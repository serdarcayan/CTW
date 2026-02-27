import json

import PySide6.QtCore as QtCore
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QGridLayout,
    QMainWindow,
    QPushButton,
    QMenu,
    QScrollArea,
    QStackedWidget,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QGroupBox,
    QFormLayout,
    QLabel,
    QLineEdit,
    QComboBox,
    QSpinBox,
)

from app.ui.app_settings.app_settings import AppSettingsPage
from PySide6.QtGui import QFont

from .create.create_new_content import CreateNewContentPage


class MainWidget(QMainWindow):
    def __init__(self, current_index=0, parent=None):
        super().__init__(parent)  # 🔥 KRİTİK SATIR

        self.current_index = current_index

        self.setWindowTitle("CTW")
        self.setMinimumSize(800, 600)

        self._create_menu()
        self._create_top_bar()
        # self._create_bottom_bar()
        self._create_central_widget()
        self._create_status_bar()

    def _create_menu(self):
        menu_bar = self.menuBar()

        user_content_menu = QMenu(
            "User Content", self
        )  # kullanıcı buradan yeni içerik oluşturacak veya var olan içeriklere erişecek / user will create new content or access existing content from here

        self.create_button = user_content_menu.addAction("Create")
        self.create_button.triggered.connect(self._go_to_create)

        self.user_content_menu_items = user_content_menu.addAction("Items")
        self.user_content_menu_items.triggered.connect(self._go_to_items)

        app_settings_menu = QMenu(
            "App Settings", self
        )  # uygulama ayarları burada olacak / app settings will be here

        general_action = app_settings_menu.addAction("General")
        general_action.triggered.connect(self._go_to_app_settings)

        app_settings_menu.addAction("Appearance")
        app_settings_menu.addAction("Shortcuts")

        help_menu = QMenu(
            "Help", self
        )  # yardım ve destek burada olacak / help and support will be here
        help_menu.addAction("Documentation")
        help_menu.addAction("About")

        others_menu = QMenu(
            "Others", self
        )  # diğer seçenekler burada olacak / other options will be here
        others_menu.addAction("Option A")
        others_menu.addAction("Option B")
        others_menu.addAction("Option C")

        menu_bar.addMenu(user_content_menu)
        menu_bar.addMenu(app_settings_menu)
        menu_bar.addMenu(help_menu)
        menu_bar.addMenu(others_menu)

    # ---------------- TOP BAR ----------------
    def _create_top_bar(self):
        pass

    # ---------------- BOTTOM BAR ----------------
    def _create_bottom_bar(self):
        self.bottomBar = QWidget()

        h_layout = QHBoxLayout(self.bottomBar)
        h_layout.setContentsMargins(10, 10, 10, 10)

        self.destroy_app_button = QPushButton("Destroy App")
        self.destroy_app_button.clicked.connect(QApplication.instance().quit)

        h_layout.addWidget(self.destroy_app_button)
        h_layout.addStretch()

    # ---------------- ITEMS PAGE ----------------
    def _items_page(self):
        from PySide6.QtWidgets import (
            QWidget,
            QVBoxLayout,
            QGridLayout,
            QLabel,
            QFrame,
            QScrollArea,
            QPlainTextEdit,
            QFormLayout,
        )
        from PySide6.QtCore import Qt
        from PySide6.QtGui import QFont
        import json

        DATA_FILE = "data/items.json"

        self.page_items = QWidget()
        main_layout = QGridLayout(self.page_items)
        main_layout.setSpacing(15)

        # ---------------------------
        # 1️⃣ SOL: CARD GRID DİKEY
        # ---------------------------
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        container = QWidget()
        card_layout = QVBoxLayout(container)  # artık dikey
        card_layout.setSpacing(15)
        scroll.setWidget(container)

        # JSON oku
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                raw_data = json.load(f)
        except Exception as e:
            print(f"Error reading {DATA_FILE}: {e} | Using default data")
            raw_data = [
                {"title": "Item 1", "desc": "Description 1"},
                {"title": "Item 2", "desc": "Description 2"},
                {"title": "Item 3", "desc": "Description 3"},
            ]

        if isinstance(raw_data, dict):
            data = [{"title": k, "desc": str(v)} for k, v in raw_data.items()]
        else:
            data = raw_data

        # Dikey kart ekleme
        for item in data:
            card = QFrame()
            card.setObjectName("card")
            card.setStyleSheet(
                """
                QFrame#card {
                    background-color: #1e1e1e;
                    border-radius: 12px;
                    padding: 14px;
                }
                QFrame#card:hover {
                    background-color: #262626;
                }
            """
            )

            layout = QVBoxLayout(card)
            layout.setSpacing(8)

            # 🔹 TITLE
            title = QLabel(item.get("title", "No Title"))
            title.setFont(QFont("Arial", 12, QFont.Weight.Bold))
            title.setStyleSheet("color: white;")
            title.setWordWrap(True)

            # 🔹 BADGE ROW (source_type + fetch_mode)
            badge_row = QHBoxLayout()

            def create_badge(text, color):
                badge = QLabel(text)
                badge.setStyleSheet(
                    f"""
                    background-color: {color};
                    color: white;
                    padding: 4px 8px;
                    border-radius: 8px;
                    font-size: 10px;
                """
                )
                return badge

            source_type = item.get("source_type", "unknown")
            fetch_mode = item.get("fetch_mode", "manual")

            badge_row.addWidget(create_badge(source_type, "#3a86ff"))
            badge_row.addWidget(create_badge(fetch_mode, "#8338ec"))
            badge_row.addStretch()

            # 🔹 URL (clickable)
            url_value = item.get("url", "")
            url = QLabel(f"<a href='{url_value}'>{url_value}</a>")
            url.setOpenExternalLinks(True)
            url.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
            url.setStyleSheet(
                """
                color: #4cc9f0;
                font-size: 11px;
            """
            )
            url.setWordWrap(True)

            # 🔹 META INFO
            duration = item.get("duration", 0)
            cache = item.get("cache_policy", "")
            created = item.get("created_at", "")

            meta = QLabel(f"⏱ {duration}s    💾 {cache}    📅 {created}")
            meta.setStyleSheet("color: #aaaaaa; font-size: 10px;")
            meta.setWordWrap(True)

            # Layout
            layout.addWidget(title)
            layout.addLayout(badge_row)
            layout.addWidget(url)
            layout.addWidget(meta)

            card_layout.addWidget(card)
        card_layout.addStretch()
        main_layout.addWidget(scroll, 0, 0, 2, 1)  # 2 satırı kapla

        # ---------------------------
        # 2️⃣ SAĞ ÜST: JSON READ-ONLY
        # ---------------------------
        json_view = QPlainTextEdit()
        json_view.setReadOnly(True)
        json_view.setFont(QFont("Consolas", 9))
        json_view.setStyleSheet(
            """
            QPlainTextEdit {
                background-color: #1e1e1e;
                color: #dcdcdc;
                border: 1px solid #444;
            }
        """
        )
        json_view.setPlainText(json.dumps(raw_data, indent=4, ensure_ascii=False))
        main_layout.addWidget(json_view, 0, 1)

        # ---------------------------
        # 3️⃣ SAĞ ALT: META PANEL
        # ---------------------------
        meta_frame = QFrame()
        meta_frame.setFrameShape(QFrame.Shape.StyledPanel)
        meta_frame.setStyleSheet(
            """
            QFrame {
                background-color: #252525;
                border: 1px solid #444;
                border-radius: 8px;
            }
            QLabel { color: #dddddd; }
        """
        )
        meta_layout = QVBoxLayout(meta_frame)
        header = QLabel("Item Meta Information")
        header.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        header.setStyleSheet("color: white;")
        meta_layout.addWidget(header)

        form_layout = QFormLayout()
        form_layout.addRow("Title:", QLabel("Example Title"))
        form_layout.addRow("Source Type:", QLabel("HTML"))
        form_layout.addRow("URL:", QLabel("https://example.com"))
        form_layout.addRow("XPath:", QLabel("//div[@class='content']"))
        form_layout.addRow("Fetch Mode:", QLabel("dynamic"))
        form_layout.addRow("Duration:", QLabel("60s"))
        form_layout.addRow("Cache Policy:", QLabel("no-cache"))
        meta_layout.addLayout(form_layout)
        meta_layout.addStretch()

        main_layout.addWidget(meta_frame, 1, 1)

        # Sütun/row stretch ayarı
        main_layout.setColumnStretch(0, 3)  # sol geniş
        main_layout.setColumnStretch(1, 2)  # sağ dar
        main_layout.setRowStretch(0, 1)
        main_layout.setRowStretch(1, 1)

        return self.page_items

    # ---------------- CENTRAL CONTENT ----------------
    def _create_central_widget(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        # 🔥 STACKED WIDGET
        self.stacked_widget = QStackedWidget()
        main_layout.addWidget(self.stacked_widget)

        # ---------------- CREATE PAGE ----------------
        self.page_create = QWidget()
        create_layout = QVBoxLayout(self.page_create)
        create_layout.addWidget(QLabel("Create Page Content"))
        create_layout.addStretch()

        # STACK’E EKLE
        self.stacked_widget.addWidget(self._items_page())  # index 0
        self.stacked_widget.addWidget(CreateNewContentPage())  # index 1
        self.stacked_widget.addWidget(AppSettingsPage())  # index 2

        self.stacked_widget.setCurrentIndex(
            self.current_index
        )  # Başlangıçta hangi sayfa gösterilecekse onun index’ini ver

        # bottom bar en altta sabit
        # main_layout.addWidget(self.bottomBar)

    # ---------------- STATUS BAR ----------------
    def _create_status_bar(self):
        self.statusBar().showMessage("Ready")
        # self.statusBar().setStyleSheet(
        #     "background-color: #f0f0f0; color: #333; padding: 5px;"
        # )
        self.statusBar().setFixedHeight(30)
        self.statusBar().setSizeGripEnabled(False)

    # ---------------- SLOT ----------------
    @QtCore.Slot()
    def _go_to_items(self):
        self.stacked_widget.setCurrentIndex(0)
        self.statusBar().showMessage("Items Page")

    @QtCore.Slot()
    def _go_to_create(self):
        self.stacked_widget.setCurrentIndex(1)
        self.statusBar().showMessage("Create Page")

    @QtCore.Slot()
    def _go_to_app_settings(self):
        self.stacked_widget.setCurrentIndex(2)
        self.statusBar().showMessage("App Settings Page")

    @QtCore.Slot()
    def on_button_clicked(self):
        x = self.x_input.value()
        y = self.y_input.value()
        text = self.line_edit.text()
        combo_value = self.combo.currentText()

        self.statusBar().showMessage(
            f"Button clicked | X={x} Y={y} | Text='{text}' | Combo='{combo_value}'"
        )
