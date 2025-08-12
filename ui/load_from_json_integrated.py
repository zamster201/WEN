
import sys
import json
import os
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QToolTip
from PySide6.QtGui import QIcon
from PySide6.QtCore import QRect, QTimer

class WENPalette(QWidget):
    def __init__(self, json_path):
        super().__init__()
        self.setWindowTitle("WEN Palette – Integrated UI")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #1e1e1e;")

        self.json_path = json_path
        self.assign_mode = False
        self.selected_button = None
        self.buttons = []
        self.data = self.load_layout()

        self.build_ui()

    def load_layout(self):
        with open(self.json_path, "r", encoding="utf-8") as f:
            return json.load(f).get("root", {}).get("cells", [])

    def build_ui(self):
        for cell in self.data:
            x = int(cell.get("x", 0))
            y = int(cell.get("y", 0))
            w = int(cell.get("width", 80))
            h = int(cell.get("height", 80))
            label = cell.get("label", "Button")
            tooltip = cell.get("tooltip", "")
            icon_path = os.path.join(os.path.dirname(__file__), "..", "resources", cell.get("icon", ""))
            cell_type = cell.get("type", "grid")
            slot_id = cell.get("slot_id", None)
            id_tag = cell.get("id_tag", "")

            btn = QPushButton(label, self)
            btn.setGeometry(QRect(x, y, w, h))
            btn.setStyleSheet("color: white; font-size: 10pt;")
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
            elif id_tag == "+" or "add" in id_tag:
                btn.clicked.connect(self.enter_assign_mode)
            elif id_tag == "save":
                btn.clicked.connect(self.save_layout)
            elif id_tag == "load":
                btn.clicked.connect(self.reload_layout)
            else:
                btn.clicked.connect(lambda: print(f"Control button '{label}' clicked."))

            self.buttons.append(btn)

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    palette = WENPalette("../data/WEN_Palette_mockup_enriched_final.drawio.json")
    palette.show()
    sys.exit(app.exec())
