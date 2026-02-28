from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, Signal


class Card(QFrame):

    clicked = Signal(dict)  # 🔥 Signal tanımı

    def __init__(self, item: dict):
        super().__init__()

        self.item = item
        self.setObjectName("card")
        self.setCursor(Qt.PointingHandCursor)  # mouse pointer değişsin

        self.setStyleSheet(
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

        self._build_ui()

    # 🔥 Mouse click override
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit(self.item)
        super().mousePressEvent(event)

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(8)

        title = QLabel(self.item.get("title", "No Title"))
        title.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        title.setStyleSheet("color: white;")
        title.setWordWrap(True)

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

        source_type = self.item.get("source_type", "unknown")
        fetch_mode = self.item.get("fetch_mode", "manual")

        badge_row.addWidget(create_badge(source_type, "#3a86ff"))
        badge_row.addWidget(create_badge(fetch_mode, "#8338ec"))
        badge_row.addStretch()

        url_value = self.item.get("url", "")
        url = QLabel(f"<a href='{url_value}'>{url_value}</a>")
        url.setOpenExternalLinks(True)
        url.setTextInteractionFlags(Qt.TextBrowserInteraction)
        url.setStyleSheet("color: #4cc9f0; font-size: 11px;")
        url.setWordWrap(True)

        duration = self.item.get("duration", 0)
        cache = self.item.get("cache_policy", "")
        created = self.item.get("created_at", "")

        meta = QLabel(f"⏱ {duration}s    💾 {cache}    📅 {created}")
        meta.setStyleSheet("color: #aaaaaa; font-size: 10px;")
        meta.setWordWrap(True)

        layout.addWidget(title)
        layout.addLayout(badge_row)
        layout.addWidget(url)
        layout.addWidget(meta)
