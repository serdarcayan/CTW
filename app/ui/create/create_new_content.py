from datetime import datetime
import json

import PySide6.QtCore as QtCore
from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QFormLayout,
    QComboBox,
    QSpinBox,
    QTextEdit,
    QGridLayout,
)


class CreateNewContentPage(QWidget):
    def __init__(self):
        super().__init__()

        # =========================
        # MODEL
        # =========================
        self._item = {
            "title": "",
            "source_type": "web",
            "fetch_mode": "manual",
            "duration": 600,
            "url": "",
            "xpaths": [],
            "cache_policy": "save_all",
            "created_at": datetime.now().isoformat(),
        }

        self.xpath_error_label = None

        # =========================
        # MAIN GRID LAYOUT
        # =========================
        main_grid = QGridLayout(self)
        main_grid.setColumnStretch(0, 3)  # Sol büyük
        main_grid.setColumnStretch(1, 2)  # Sağ küçük

        # =========================
        # LEFT SIDE (FORM AREA)
        # =========================
        left_container = QWidget()
        left_layout = QVBoxLayout(left_container)

        header = QLabel("Create New Remember Content")
        header.setStyleSheet("font-weight: bold; font-size: 16px;")
        left_layout.addWidget(header)

        form_container = QWidget()
        form_layout = QFormLayout(form_container)
        form_layout.setVerticalSpacing(12)
        form_layout.setHorizontalSpacing(10)

        # -------- TITLE ----------
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Enter title here")
        self.title_input.textChanged.connect(
            lambda text: self._update_item("title", text)
        )
        form_layout.addRow("Title:", self.title_input)

        # -------- SOURCE TYPE ----------
        self.source_type_input = QComboBox()
        self.source_type_input.addItems(["web", "api", "local_file"])
        self.source_type_input.currentTextChanged.connect(
            lambda text: self._update_item("source_type", text)
        )
        form_layout.addRow("Source Type:", self.source_type_input)

        # -------- FETCH MODE ----------
        self.fetch_mode_input = QComboBox()
        self.fetch_mode_input.addItems(["manual", "scheduled"])
        self.fetch_mode_input.currentTextChanged.connect(self._on_fetch_mode_changed)
        form_layout.addRow("Fetch Mode:", self.fetch_mode_input)

        # -------- DURATION ----------
        self.duration_input = QSpinBox()
        self.duration_input.setRange(10, 999999)
        self.duration_input.setSuffix(" sec")
        self.duration_input.setValue(self._item["duration"])
        self.duration_input.setEnabled(False)
        self.duration_input.valueChanged.connect(
            lambda val: self._update_item("duration", val)
        )
        form_layout.addRow("Duration:", self.duration_input)

        # -------- URL ----------
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("https://example.com")
        self.url_input.textChanged.connect(lambda text: self._update_item("url", text))
        form_layout.addRow("URL:", self.url_input)

        # -------- XPATHS ----------
        self.xpath_container = QVBoxLayout()
        self.xpath_container.setSpacing(6)
        self.xpath_inputs = []

        add_xpath_btn = QPushButton("+ Add XPath")
        add_xpath_btn.clicked.connect(lambda: self._add_xpath_input())

        form_layout.addRow("XPaths:", self.xpath_container)
        form_layout.addRow("", add_xpath_btn)

        # -------- CACHE POLICY ----------
        self.cache_policy_input = QComboBox()
        self.cache_policy_input.addItems(["save_all", "save_new", "no_cache"])
        self.cache_policy_input.currentTextChanged.connect(
            lambda text: self._update_item("cache_policy", text)
        )
        form_layout.addRow("Cache Policy:", self.cache_policy_input)

        left_layout.addWidget(form_container)
        left_layout.addStretch()

        # ------- BUTTONS ----------
        button_container = QWidget()
        button_layout = QHBoxLayout(button_container)
        save_btn = QPushButton("Save")
        save_btn.clicked.connect(lambda: self._save_content(self._item))
        cancel_btn = QPushButton("Cancel")
        button_layout.addWidget(save_btn)
        button_layout.addWidget(cancel_btn)
        left_layout.addWidget(button_container)

        # =========================
        # RIGHT TOP (JSON PREVIEW)
        # =========================
        json_container = QWidget()
        json_layout = QVBoxLayout(json_container)

        json_label = QLabel("Live JSON Preview")
        json_label.setStyleSheet("font-weight: bold;")
        json_layout.addWidget(json_label)

        self.json_preview = QTextEdit()
        self.json_preview.setReadOnly(True)
        self.json_preview.setStyleSheet(
            "background-color: #1e1e1e; color: #00ff99; font-family: Consolas;"
        )
        json_layout.addWidget(self.json_preview)

        # İlk JSON bas
        self._refresh_json_preview()

        # =========================
        # RIGHT BOTTOM (EMPTY)
        # =========================
        bottom_placeholder = QWidget()

        # =========================
        # GRID PLACEMENT
        # =========================
        main_grid.addWidget(left_container, 0, 0, 2, 1)  # Sol tüm yüksekliği kaplar
        main_grid.addWidget(json_container, 0, 1)  # Sağ üst JSON
        main_grid.addWidget(bottom_placeholder, 1, 1)  # Sağ alt boş

    # =========================================================
    # MODEL UPDATE + JSON REFRESH
    # =========================================================
    def _update_item(self, key, value):
        self._item[key] = value
        self._refresh_json_preview()

    def _refresh_json_preview(self):
        pretty_json = json.dumps(self._item, indent=4, ensure_ascii=False)
        self.json_preview.setText(pretty_json)

    # =========================================================
    # FETCH MODE
    # =========================================================
    def _on_fetch_mode_changed(self, mode):
        self._item["fetch_mode"] = mode

        if mode == "scheduled":
            self.duration_input.setEnabled(True)
        else:
            self.duration_input.setEnabled(False)

        self._refresh_json_preview()

    # =========================================================
    # XPATH EKLE
    # =========================================================
    def _add_xpath_input(self, value=""):

        # =====================================================
        # VALIDATION
        # =====================================================

        error_message = None

        if self._item["source_type"] != "web":
            error_message = "XPaths only available for 'web' source type."

        elif not self._item["url"].strip():
            error_message = "Please enter a URL before adding XPaths."

        elif len(self.xpath_inputs) >= 4:
            error_message = "Maximum 4 XPaths allowed."

        # =====================================================
        # ERROR VARSA
        # =====================================================

        if error_message:
            self._show_xpath_error(error_message)
            return

        # =====================================================
        # HATA YOKSA DEVAM
        # =====================================================

        self._clear_xpath_error()

        row_widget = QWidget()
        row_layout = QHBoxLayout(row_widget)
        row_layout.setContentsMargins(0, 0, 0, 0)

        xpath_input = QLineEdit()
        xpath_input.setPlaceholderText("//div[@class='example']")
        xpath_input.setText(value)
        xpath_input.textChanged.connect(self._update_xpaths)

        remove_btn = QPushButton("✕")
        remove_btn.setFixedWidth(30)
        remove_btn.clicked.connect(
            lambda: self._remove_xpath_input(row_widget, xpath_input)
        )

        row_layout.addWidget(xpath_input)
        row_layout.addWidget(remove_btn)

        self.xpath_container.addWidget(row_widget)
        self.xpath_inputs.append(xpath_input)

        self._update_xpaths()

    # =========================================================
    # ERROR LABEL YÖNETİMİ
    # =========================================================

    def _show_xpath_error(self, message):
        if not self.xpath_error_label:
            self.xpath_error_label = QLabel()
            self.xpath_error_label.setStyleSheet("color: red; font-size: 12px;")
            self.xpath_container.addWidget(self.xpath_error_label)

        self.xpath_error_label.setText(message)

    def _clear_xpath_error(self):
        if self.xpath_error_label:
            self.xpath_container.removeWidget(self.xpath_error_label)
            self.xpath_error_label.deleteLater()
            self.xpath_error_label = None

    # =========================================================
    # MODEL UPDATE
    # =========================================================

    def _update_xpaths(self):
        self._item["xpaths"] = [
            inp.text().strip() for inp in self.xpath_inputs if inp.text().strip()
        ]
        self._refresh_json_preview()

    # =========================================================
    # REMOVE
    # =========================================================

    def _remove_xpath_input(self, row_widget, xpath_input):
        self.xpath_container.removeWidget(row_widget)
        row_widget.deleteLater()

        if xpath_input in self.xpath_inputs:
            self.xpath_inputs.remove(xpath_input)

        self._clear_xpath_error()
        self._update_xpaths()




    # =========================================================
    @QtCore.Slot()
    def _save_content(self, item):
        from app.models.content_model import ContentModel
        
        ContentModel(item=item).create()
