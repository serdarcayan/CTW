from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QGraphicsDropShadowEffect,
)
from PySide6.QtGui import QFont, QColor
from PySide6.QtCore import Qt, Signal
from app.ui import theme


class Card(QFrame):

    clicked = Signal(dict)  # 🔥 Signal tanımı

    def __init__(self, item: dict):
        super().__init__()

        # subtle drop shadow for a raised card effect
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(12)
        shadow.setOffset(0, 2)
        shadow.setColor(QColor(0, 0, 0, 160))
        self.setGraphicsEffect(shadow)

        self.item = item
        self.setObjectName("card")
        self.setCursor(Qt.PointingHandCursor)  # mouse pointer değişsin

        self.setStyleSheet(f"""
            QFrame#card {{
                background-color: {theme.SURFACE};
                border: 1px solid {theme.BORDER_DEFAULT};
                border-radius: {theme.RADIUS_LARGE}px;
                padding: 14px;
            }}
            QFrame#card:hover {{
                background-color: {theme.SURFACE_HOVER};
                border: 1px solid {theme.BORDER_DEFAULT};
            }}
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
        title.setStyleSheet(f"color: {theme.TEXT_PRIMARY};background-color: transparent;")
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

        # map types to theme badge colors
        color_map = {
            "api": theme.BADGE_API,
            "scraper": theme.BADGE_SCRAPER,
            "cache": theme.BADGE_CACHE,
            "manual": theme.BADGE_MANUAL,
        }

        badge_row.addWidget(create_badge(source_type, color_map.get(source_type, theme.BADGE_API)))
        badge_row.addWidget(create_badge(fetch_mode, color_map.get(fetch_mode, theme.BADGE_MANUAL)))
        badge_row.addStretch()

        url_value = self.item.get("url", "")
        url = QLabel(f"<a href='{url_value}'>{url_value}</a>")
        url.setOpenExternalLinks(True)
        url.setTextInteractionFlags(Qt.TextBrowserInteraction)
        url.setStyleSheet(f"color: {theme.ACCENT_PRIMARY}; font-size: 11px; background-color: transparent;")
        url.setWordWrap(True)

        duration = self.item.get("duration", 0)
        cache = self.item.get("cache_policy", "")
        created = self.item.get("created_at", "")

        meta = QLabel(f"⏱ {duration}s    💾 {cache}    📅 {created}")
        meta.setStyleSheet(f"color: {theme.TEXT_SECONDARY}; font-size: 10px; background-color: transparent;")
        meta.setWordWrap(True)

        layout.addWidget(title)
        layout.addLayout(badge_row)
        layout.addWidget(url)
        layout.addWidget(meta)
