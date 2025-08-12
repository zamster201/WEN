
import sys
import json
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PySide6.QtGui import QIcon
from PySide6.QtCore import QRect, QTimer, Qt
from wen.core.utils.get_data_path import get_data_path
from wen.core.branding import get_inter_font, get_theme_stylesheet
from wen.core.branding import get_icon
from wen.core.highlight_manager import Highlight_Manager
class WENPalette(QWidget):
    def __init__(self, json_path):
        super().__init__()
        self.setWindowFlags(
            Qt.Window |
            Qt.WindowTitleHint |
            Qt.WindowSystemMenuHint |
            Qt.WindowMinMaxButtonsHint
        )
        self.setWindowTitle("WEN Palette – Dynamic Grid from JSON")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #1e1e1e;")

        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

           # Position in upper-left
            screen_geometry = QApplication.primaryScreen().geometry()
            screen_width = screen_geometry.width()
            x = screen_geometry.x() + 20   # 20px from left edge of primary screen
            y = screen_geometry.y() + 20   # 20px from top

            # Set window geometry
            self.setGeometry(20, 20, default_width, default_height)
            # self.setFixedSize(self.size())

        self.buttons = []   # <-- What does this do ?

        for cell in data["root"]["cells"]:
            x = int(cell.get("x", 0))
            y = int(cell.get("y", 0))
            w = int(cell.get("width", 80))
            h = int(cell.get("height", 80))
            label = cell.get("label", "Button")
            tooltip = cell.get("tooltip", "")
            icon_path = cell.get("icon", "")
            cell_type = cell.get("type", "grid")

            btn = QPushButton(label, self)
            btn.setGeometry(QRect(x, y, w, h))
            btn.setStyleSheet("color: white; font-size: 10pt;")
            if icon_path and icon_path != "default.ico":
                btn.setIcon(QIcon(icon_path))
                btn.setIconSize(btn.size() * 0.6)

            # Tooltip delay logic (for grid buttons only)
            if tooltip and cell_type == "grid":
                def show_tooltip(b=btn, t=tooltip):
                    QToolTip.showText(b.mapToGlobal(b.rect().center()), t)
                btn.enterEvent = lambda event, f=show_tooltip: QTimer.singleShot(800, f)

            self.buttons.append(btn)

            self.adjustSize()  # Call this after all widgets are added
#           self.setFixedSize(self.sizeHint())  # Locks the window to fit content
            # Calculate default size from JSON content

            max_x = max(cell["x"] + cell["width"] for cell in data["root"]["cells"])
            max_y = max(cell["y"] + cell["height"] for cell in data["root"]["cells"])
            default_width = max_x + 20
            default_height = max_y + 20



if __name__ == "__main__":
    app = QApplication(sys.argv)
#    app.setStyleSheet(get_theme_stylesheet())
#    app.setFont(get_inter_font(size=10, bold=False))  # Or size=11, bold=True, etc.
    window = WENPalette(get_data_path("WEN_palette_runtime_layout_default.json"))

    window.show()

    QTimer.singleShot(15000, app.quit)  # auto-quit after 15 seconds
    sys.exit(app.exec())
