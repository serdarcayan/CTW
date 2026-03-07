from app.ui.components.card import Card
from app.ui.components.infoPanel import MetaInfoWidget
from app.ui.components.jsonViewer import JsonViewer
from PySide6.QtWidgets import (
    QHBoxLayout,
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QLabel,
    QFrame,
    QScrollArea,
    QPlainTextEdit,
    QFormLayout,
)
from app.ui import theme
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont
import json


class ItemsPage(QWidget):
    item_selected = Signal(dict)

    DATA_FILE = "data/items.json"

    def __init__(self, parent=None):
        super().__init__(parent)
        self._build_ui()

    def _load_data(self):
        try:
            with open(self.DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return [
                {"title": "Item 1", "desc": "Description 1"},
                {"title": "Item 2", "desc": "Description 2"},
                {"title": "Item 3", "desc": "Description 3"},
            ]

    def _build_ui(self):
        # Ana dikey layout: içerik + bottom bar
        main_layout = QVBoxLayout(self)

        # ÜST: GRID (sol kartlar, sağ json/meta)
        grid = QGridLayout()
        raw_data = self._load_data()

        # SOL: kartlar
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        container = QWidget()
        card_layout = QVBoxLayout(container)
        for item in raw_data:
            card = Card(item)
            card.clicked.connect(self._on_card_clicked)
            card_layout.addWidget(card)
        card_layout.addStretch()
        scroll.setWidget(container)

        # SAĞ: üst-alt layout
        self.json_viewer = JsonViewer(raw_data)
        self.meta_viewer = MetaInfoWidget(raw_data[0] if raw_data else {})
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.json_viewer)
        right_layout.addWidget(self.meta_viewer)
        right_layout.setStretch(0, 2)
        right_layout.setStretch(1, 1)
        right_container = QWidget()
        right_container.setLayout(right_layout)

        # GRID içine ekle
        grid.addWidget(scroll, 0, 0)
        grid.addWidget(right_container, 0, 1)
        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)

        main_layout.addLayout(grid)

        # ALT: Bottom Bar
        bottom_bar = QFrame()
        bottom_bar.setStyleSheet(f"""
            QFrame {{
                background-color: {theme.SURFACE};
                border: 1px solid {theme.BORDER_DEFAULT};
                border-radius: {theme.RADIUS_LARGE}px;
            }}
            QLabel {{ color: {theme.TEXT_PRIMARY}; }}
            """
        )
        bar_layout = QHBoxLayout(bottom_bar)

        # Örnek butonlar
        view_raw_btn = QLabel("View Raw")
        view_raw_btn.setFont(QFont("Arial", 10, QFont.Bold))
        view_raw_btn.setProperty('class', 'accent')
        save_btn = QLabel("Save")
        save_btn.setFont(QFont("Arial", 10, QFont.Bold))
        save_btn.setProperty('class', 'accent')

        bar_layout.addWidget(view_raw_btn)
        bar_layout.addWidget(save_btn)
        bar_layout.addStretch()

        main_layout.addWidget(bottom_bar)
    # def _bottom_bar(self):
    #     bar = QFrame()
    #     bar.setStyleSheet(
    #         """
    #         QFrame {
    #             background-color: #252525;
    #             border: 1px solid #444;
    #             border-radius: 8px;
    #         }
    #         QLabel { color: #dddddd; }
    #     """
    #     )
    #     layout = QHBoxLayout(bar)
        
    #     view_raw_btn = QLabel("View Raw")
    #     view_raw_btn.setFont(QFont("Arial", 10, QFont.Bold))
    #     view_raw_btn.setStyleSheet("color: #00aaff;")
    #     layout.addWidget(view_raw_btn)
    #     layout.addStretch()
        
    
    
    def _on_card_clicked(self, item):
        self.json_viewer.setPlainText(json.dumps(item, indent=4, ensure_ascii=False))
        self.item_selected.emit(item)
