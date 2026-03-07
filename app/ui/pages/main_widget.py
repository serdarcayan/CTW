import sys
import PySide6.QtCore as QtCore
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QStackedWidget,
)
from PySide6.QtGui import QIcon

from app.ui.pages.app_settings.app_settings import AppSettingsPage
from app.ui.pages.create.create_new_content import CreateNewContentPage
from app.ui.pages.items.items import ItemsPage
from app.ui.components.Custom_CTW_appbar import CustomCTWAppBar


# =========================================================
# 🔹 MAIN WINDOW (CONTROLLER)
# =========================================================
class MainWidget(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("CTW")
        self.setMinimumSize(900, 600)

        # Custom AppBar
        self.custom_bar = CustomCTWAppBar(self)
        self.custom_bar.items_clicked.connect(lambda: self.go_to("items"))
        self.custom_bar.create_clicked.connect(lambda: self.go_to("create"))
        self.custom_bar.settings_clicked.connect(lambda: self.go_to("settings"))

        self.setMenuWidget(self.custom_bar)

        self._create_central_widget()
        self._create_status_bar()

    # =====================================================
    # CENTRAL AREA
    # =====================================================

    def _create_central_widget(self):

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        self.stacked = QStackedWidget()
        layout.addWidget(self.stacked)

        # Pages
        self.pages = {
            "items": ItemsPage(),
            "create": CreateNewContentPage(),
            "settings": AppSettingsPage(),
        }

        # stacked içine ekle
        for page in self.pages.values():
            self.stacked.addWidget(page)

        # signal bağlantısı
        self.pages["items"].item_selected.connect(self._on_item_selected)

        # başlangıç sayfası
        self.go_to("items")

    # =====================================================
    # STATUS BAR
    # =====================================================

    def _create_status_bar(self):
        self.statusBar().showMessage("Ready")

    # =====================================================
    # ROUTER
    # =====================================================

    def go_to(self, page_name):

        page = self.pages.get(page_name)

        if page:
            self.stacked.setCurrentWidget(page)

    # =====================================================
    # EVENTS
    # =====================================================

    # @QtCore.Slot()
    # def _go_to_settings(self):
    #     self.statusBar().showMessage("Settings clicked")

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
