import sys
from PySide6 import QtWidgets
from app.ui.main_widget import MainWidget


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWidget(current_index=0)
    window.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()