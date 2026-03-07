import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from app.ui.pages.main_widget import MainWidget
from app.ui import theme

from app.core.cache_manager import CacheManager


def main():

    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon("assets/icons/CTW_icon.png"))
    app.setStyle("Fusion")
    app.setStyleSheet(theme.get_stylesheet())

    # database init
    cache_manager = CacheManager()

    window = MainWidget()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
