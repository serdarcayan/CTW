from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QVBoxLayout,
    QLabel,
    QFrame,
    QFormLayout,
)


class MetaInfoWidget(QFrame):
    def __init__(self):
        super().__init__()
        self._setup_style()
        self._build_ui()

    def _setup_style(self):
        self.setStyleSheet(
            """
            QFrame {
                background-color: #252525;
                border: 1px solid #444;
                border-radius: 8px;
            }
            QLabel { color: #dddddd; }
        """
        )

    def _build_ui(self):
        layout = QVBoxLayout(self)

        header = QLabel("Item Meta Information")
        header.setFont(QFont("Arial", 12, QFont.Bold))
        header.setStyleSheet("color: white;")
        layout.addWidget(header)

        self.form = QFormLayout()

        self.title_label = QLabel("-")
        self.url_label = QLabel("-")

        self.form.addRow("Title:", self.title_label)
        self.form.addRow("URL:", self.url_label)

        layout.addLayout(self.form)
        layout.addStretch()

    def update_meta(self, item: dict):
        self.title_label.setText(item.get("title", "-"))
        self.url_label.setText(item.get("url", "-"))
