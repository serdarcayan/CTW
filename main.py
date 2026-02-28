import sys
from PySide6 import QtWidgets
from app.ui.pages.main_widget import MainWidget


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWidget()
    window.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()