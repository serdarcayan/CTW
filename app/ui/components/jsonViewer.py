import json
from PySide6.QtGui import QFont
from app.ui import theme
from PySide6.QtWidgets import QPlainTextEdit


class JsonViewer(QPlainTextEdit):
    def __init__(self, data):
        super().__init__()
        self.setReadOnly(True)
        self.setFont(QFont("Consolas", 9))
        self.setStyleSheet(f"""
            QPlainTextEdit {{
                background-color: {theme.SURFACE};
                color: {theme.TEXT_PRIMARY};
                border: 1px solid {theme.BORDER_DEFAULT};
            }}
        """
        )
        self.setPlainText(json.dumps(data, indent=4, ensure_ascii=False))
