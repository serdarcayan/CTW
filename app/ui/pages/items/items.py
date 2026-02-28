from app.ui.components.card import Card
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
        main_layout = QGridLayout(self)
        raw_data = self._load_data()

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        container = QWidget()
        card_layout = QVBoxLayout(container)

        for item in raw_data:
            card = Card(item)
            card.clicked.connect(self._on_card_clicked)  # 🔥 kritik
            card_layout.addWidget(card)

        card_layout.addStretch()
        scroll.setWidget(container)

        main_layout.addWidget(scroll, 0, 0)

    def _on_card_clicked(self, item):
        self.item_selected.emit(item)
