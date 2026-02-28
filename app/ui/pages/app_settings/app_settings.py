import PySide6.QtCore as QtCore
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QFormLayout,
    QGroupBox,
    QLabel,
    QLineEdit,
    QComboBox,
    QSpinBox,
    QHBoxLayout,
    QPushButton,
)


class AppSettingsPage(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)

        # Başlık
        label = QLabel("🆕 APP SETTINGS PAGE")
        main_layout.addWidget(label)

        # ---------------- FORM ALANI ----------------
        form_group_box = QGroupBox("Form layout")
        form_layout = QFormLayout(form_group_box)

        self.line_edit = QLineEdit()
        self.combo = QComboBox()
        self.combo.addItems(["Option 1", "Option 2", "Option 3"])

        form_layout.addRow("Line 1:", self.line_edit)
        form_layout.addRow("Line 2:", self.combo)

        # X ve Y yan yana
        xy_widget = QWidget()
        xy_layout = QHBoxLayout(xy_widget)
        xy_layout.setContentsMargins(0, 0, 0, 0)

        self.x_input = QSpinBox()
        self.x_input.setRange(0, 1000)

        self.y_input = QSpinBox()
        self.y_input.setRange(0, 1000)

        xy_layout.addWidget(QLabel("X:"))
        xy_layout.addWidget(self.x_input)
        xy_layout.addSpacing(15)
        xy_layout.addWidget(QLabel("Y:"))
        xy_layout.addWidget(self.y_input)

        form_layout.addRow("Coordinates:", xy_widget)

        main_layout.addWidget(form_group_box)

        # ---------------- BUTON ----------------
        self.button = QPushButton("Deneme")
        self.button.clicked.connect(self.on_button_clicked)
        main_layout.addWidget(self.button)

        main_layout.addStretch()

    # ---------------- SLOT ----------------
    def on_button_clicked(self):
        x = self.x_input.value()
        y = self.y_input.value()
        text = self.line_edit.text()
        combo_value = self.combo.currentText()

        print(f"AppSettings | X={x} Y={y} | Text='{text}' | Combo='{combo_value}'")
        
    def settings_bottom_bar(self):
        layout = QHBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignRight)
        save_btn = QPushButton("Start widget")
        

    def read_config(self): #TODO: config dosyasını oku ve widgetlara uygula
        pass
