from PySide6.QtWidgets import QMenuBar, QWidget, QHBoxLayout, QPushButton, QLabel
from PySide6.QtGui import QIcon, QFont
from app.ui import theme
from PySide6.QtCore import Signal, Qt, QSize


class CustomCTWAppBar(QWidget):
    items_clicked = Signal()
    create_clicked = Signal()
    settings_clicked = Signal()

    styles = f"""
        QWidget {{
            background-color: {theme.SURFACE};
            color: {theme.TEXT_PRIMARY};
            padding: 4px 8px;
        }}

        QPushButton {{
            background-color: transparent;
            border: none;
            color: {theme.TEXT_PRIMARY};
            padding: 4px 8px;
        }}

        QPushButton:hover {{
            background-color: {theme.SURFACE_HOVER};
            color: {theme.TEXT_PRIMARY};
            border-radius: 4px;
        }}

        QPushButton:pressed {{
            background-color: {theme.BORDER_DEFAULT};
            color: {theme.TEXT_PRIMARY};
        }}
        """

    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet(self.styles)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 2, 5, 2)
        layout.setSpacing(10)

        # Sol ikon
        icon_label = QPushButton()
        icon_label.setIcon(QIcon("assets/icons/CTW_icon.png"))
        icon_label.setIconSize(QSize(24, 24))
        icon_label.setFlat(True)
        icon_label.setEnabled(True)
        layout.addWidget(icon_label)

        # Başlık
        title = QPushButton("CTW")
        title.setFont(QFont("Arial", 12, QFont.Bold))
        title.setFlat(True)
        title.setEnabled(False)
        layout.addWidget(title)

        layout.addStretch()

        # Items butonu
        items_btn = QPushButton("Items")
        items_btn.setIcon(QIcon("assets/items.png"))
        items_btn.setFont(QFont("Arial", 10))
        items_btn.clicked.connect(self.items_clicked.emit)
        layout.addWidget(items_btn)
        
        create_new_content_btn = QPushButton("Create")
        create_new_content_btn.setIcon(QIcon("assets/create.png"))
        create_new_content_btn.setFont(QFont("Arial", 10))
        create_new_content_btn.clicked.connect(self.create_clicked.emit)
        layout.addWidget(create_new_content_btn)

        # Settings butonu
        settings_btn = QPushButton("Settings")
        settings_btn.setIcon(QIcon("assets/settings.png"))
        settings_btn.setFont(QFont("Arial", 10))
        settings_btn.clicked.connect(self.settings_clicked.emit)
        layout.addWidget(settings_btn)

        # self.setFixedHeight(40)
