import sys
import PySide6.QtCore as QtCore
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QFrame,
    QFormLayout,
    QMenu,
    QStackedWidget,
)

from app.ui.components.card import Card
from app.ui.pages.items.items import ItemsPage

# =========================================================
# 🔹 MAIN WINDOW (CONTROLLER)
# =========================================================
class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CTW")
        self.setMinimumSize(900, 600)

        self._create_menu()
        self._create_central_widget()
        self._create_status_bar()

    def _create_menu(self):
        menu_bar = self.menuBar()

        user_menu = QMenu("User Content", self)

        items_action = user_menu.addAction("Items")
        items_action.triggered.connect(self._go_to_items)

        menu_bar.addMenu(user_menu)

    def _create_central_widget(self):
        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        self.stacked = QStackedWidget()
        layout.addWidget(self.stacked)

        # Pages
        self.items_page = ItemsPage()
        self.items_page.item_selected.connect(self._on_item_selected)

        self.stacked.addWidget(self.items_page)

    def _create_status_bar(self):
        self.statusBar().showMessage("Ready")

    @QtCore.Slot()
    def _go_to_items(self):
        self.stacked.setCurrentIndex(0)

    @QtCore.Slot(dict)
    def _on_item_selected(self, item):
        self.statusBar().showMessage(f"Selected: {item.get('title')}")


# =========================================================
# 🔹 ENTRY POINT
# =========================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWidget()
    window.show()
    sys.exit(app.exec())
