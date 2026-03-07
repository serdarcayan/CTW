from PySide6.QtGui import QFont, Qt
from app.ui import theme
from PySide6.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QFrame,
    QFormLayout,
)


class MetaInfoWidget(QFrame):
    def __init__(self, data=None):
        super().__init__()
        self._setup_style()
        self._build_ui()
        if data:
            self.update_meta(data)

    def _setup_style(self):
        self.setStyleSheet(f"""
            QFrame {{
                background-color: {theme.SURFACE};
                border: 1px solid {theme.BORDER_DEFAULT};
                border-radius: {theme.RADIUS_LARGE}px;
            }}
            QLabel {{ color: {theme.TEXT_PRIMARY}; }}
        """
        )

    def _build_ui(self):
        layout = QVBoxLayout(self)

        header = QLabel("Item Meta Information")
        header.setFont(QFont("Arial", 12, QFont.Bold))
        header.setStyleSheet(f"color: {theme.ACCENT_PRIMARY};")
        layout.addWidget(header)

        self.form = QFormLayout()

        self.title_label = QLabel("-")
        self.url_label = QLabel("-")

        title_layout = QHBoxLayout()
        title_layout.addWidget(self.title_label)
        title_layout.addStretch()

        self.form.addRow("Title:", title_layout)
        self.form.addRow("URL:", self.url_label)

        layout.addLayout(self.form)

        # 🔹 Empty state label
        self.empty_label = QLabel("No meta information available")
        self.empty_label.setAlignment(Qt.AlignCenter)
        self.empty_label.setStyleSheet(
            f"color: {theme.TEXT_SECONDARY}; font-style: italic;"
        )

        layout.addWidget(self.empty_label)
        layout.addStretch()

        self.empty_label.hide()  # başlangıçta gizli


    def update_meta(self, item: dict):

        self.form.setEnabled(True)
        self.empty_label.hide()

        self.title_label.setText(item.get("title", "-"))
        self.url_label.setText(item.get("url", "-"))

    def has_no_data(self):
        self.form.setEnabled(False)
        self.title_label.setText("-")
        self.url_label.setText("-")

        self.empty_label.show()
