import json
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QPlainTextEdit


class JsonViewer(QPlainTextEdit):
    def __init__(self, data):
        super().__init__()
        self.setReadOnly(True)
        self.setFont(QFont("Consolas", 9))
        self.setStyleSheet(
            """
            QPlainTextEdit {
                background-color: #1e1e1e;
                color: #dcdcdc;
                border: 1px solid #444;
            }
        """
        )
        self.setPlainText(json.dumps(data, indent=4, ensure_ascii=False))
