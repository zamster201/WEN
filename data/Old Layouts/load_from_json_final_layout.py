
import sys
import json
import os
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QFileDialog, QToolTip, QListWidget
)
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import QRect, QTimer

class WENPalette(QWidget):
    def __init__(self, json_path):
        super().__init__()
        self.setWindowTitle("WEN Palette – Final Layout Preview")
        self.setGeometry(100, 100, 650, 700)
        self.setStyleSheet("background-color: #1a1a1a;")

        self.theme = "dark"
        self.assign_mode = False
        self.selected_button = None
        self.buttons = []
        self.json_path = json_path
        self.data = self.load_layout()

        self.build_ui()
        self.apply_theme()

    def load_layout(self):
        with open(self.json_path, "r", encoding="utf-8") as f:
            return json.load(f).get("root", {}).get("cells", [])

    def build_ui(self):
        grid_btn_count = 0
        for cell in self.data:
            x = int(cell.get("x", 0))
            y = int(cell.get("y", 0))
            w = int(cell.get("width", 80))
            h = int(cell.get("height", 80))
            label = cell.get("label", "*") or "*"
            tooltip = cell.get("tooltip", "")
            icon_path = os.path.join(os.path.dirname(__file__), "..", "resources", cell.get("icon", ""))
            cell_type = cell.get("type", "grid")
            slot_id = cell.get("slot_id", None)
            id_tag = cell.get("id_tag", "")

            btn = QPushButton(label, self)
            btn.setGeometry(QRect(x, y, w, h))
            btn.setFont(QFont("Arial", 10))
            btn.setStyleSheet("color: white; font-size: 10pt; border: 1px solid gray; border-radius: 6px;")
            btn.setObjectName(f"btn_{slot_id or id_tag}")

            if os.path.exists(icon_path) and cell.get("icon") != "default.ico":
                btn.setIcon(QIcon(icon_path))
                btn.setIconSize(btn.size() * 0.6)

            if tooltip and cell_type == "grid":
                def show_tooltip(b=btn, t=tooltip):
                    QToolTip.showText(b.mapToGlobal(b.rect().center()), t)
                btn.enterEvent = lambda event, f=show_tooltip: QTimer.singleShot(800, f)

            if cell_type == "grid":
                btn.clicked.connect(lambda checked, b=btn: self.handle_grid_click(b))
                grid_btn_count += 1
            elif id_tag == "+":
                btn.setText("+")
                btn.setToolTip("Add Application to Button")
                btn.clicked.connect(self.enter_assign_mode)
            elif id_tag == "-":
                btn.setText("-")
                btn.setToolTip("Remove Application from Button")
                btn.clicked.connect(lambda: print("Remove action not yet implemented."))
            elif "3x3" in id_tag:
                btn.setText("3 x 3")
                btn.setToolTip("Toggle between 3x3 and 4x4 Layouts")
                btn.clicked.connect(lambda: print("Layout toggle not yet implemented."))
            elif id_tag == "save":
                btn.setText("Save")
                btn.clicked.connect(self.save_layout)
            elif id_tag == "load":
                btn.setText("Load")
                btn.clicked.connect(self.reload_layout)
            else:
                continue

            self.buttons.append(btn)

        # Light/Dark mode toggle
        theme_btn = QPushButton("☀️ / 🌙", self)
        theme_btn.setGeometry(QRect(480, 20, 60, 30))
        theme_btn.clicked.connect(self.toggle_theme)
        theme_btn.setToolTip("Toggle Light / Dark Mode")
        self.buttons.append(theme_btn)

        # Save and Load list boxes
        self.save_list = QListWidget(self)
        self.save_list.setGeometry(40, 600, 250, 60)
        self.save_list.setStyleSheet("background-color: white;")

        self.load_list = QListWidget(self)
        self.load_list.setGeometry(320, 600, 250, 60)
        self.load_list.setStyleSheet("background-color: white;")

    def handle_grid_click(self, button):
        if self.assign_mode:
            self.selected_button = button
            self.assign_mode = False
            self.assign_app_to_button(button)
        else:
            print(f"Clicked: {button.text()}")

    def enter_assign_mode(self):
        print("Assignment mode activated. Click a grid button to assign an app.")
        self.assign_mode = True

    def assign_app_to_button(self, button):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Application", "", "Executable (*.exe);;All Files (*)")
        if file_path:
            app_name = os.path.basename(file_path)
            button.setToolTip(file_path)
            button.setText(app_name.split(".")[0])
            print(f"Assigned: {app_name} → {button.objectName()}")

    def save_layout(self):
        print("Save layout clicked — TODO: implement saving")

    def reload_layout(self):
        print("Reload layout clicked — TODO: implement reloading")

    def toggle_theme(self):
        self.theme = "light" if self.theme == "dark" else "dark"
        self.apply_theme()

    def apply_theme(self):
        if self.theme == "light":
            self.setStyleSheet("background-color: #f0f0f0;")
            for btn in self.buttons:
                btn.setStyleSheet("color: black; font-size: 10pt; border: 1px solid gray; border-radius: 6px;")
        else:
            self.setStyleSheet("background-color: #1a1a1a;")
            for btn in self.buttons:
                btn.setStyleSheet("color: white; font-size: 10pt; border: 1px solid gray; border-radius: 6px;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    json_file = os.path.join(os.path.dirname(__file__), "..", "..", "data", "WEN_Palette_mockup_final_fixed_blanklabels.json")
    window = WENPalette(json_file)
    window.show()
    sys.exit(app.exec())
