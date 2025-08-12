
import sys
import json
import os
sys.path.insert(0, os.path.dirname(__file__))
from pathlib import Path

from core.get_data_path import get_data_path
from core.branding import get_inter_font, get_theme_stylesheet
from core.branding import get_icon
from core.theme_manager import ThemeManager
from core.theme_utils import highlight_buttons, clear_highlights

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PySide6.QtWidgets import QGridLayout, QLabel, QSpacerItem, QSizePolicy, QHBoxLayout
from PySide6.QtCore import Qt, QRect, QTimer, QSize
from PySide6.QtGui import QIcon, QFont, QColor, QPalette


class WENPalette(QWidget):
    def __init__(self, json_path, theme_mgr=None):
        super().__init__()
        print("[WEN INIT] Starting init sequence...")

        # WEN branding
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#1C1F26"))
        palette.setColor(QPalette.Button, QColor("#C2C7CC"))
        palette.setColor(QPalette.ButtonText, Qt.black)
        palette.setColor(QPalette.WindowText, QColor("#00D1FF"))
        palette.setColor(QPalette.Text, Qt.white)
        QApplication.instance().setPalette(palette)
        QApplication.instance().setFont(QFont("Inter", 10))

        self.setWindowFlags(
            Qt.Window | Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMinMaxButtonsHint
        )
        self.setWindowTitle("WEN")
        self.setStyleSheet("QWidget { color: #00D1FF; }")

        self.theme_mgr = theme_mgr
        self.current_theme = "dark"

        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.layout_data = data

        self.setFixedSize(255, 275)

        self.add_mode = False
        self.add_timer = QTimer()
        self.add_timer.setSingleShot(True)
        self.add_timer.timeout.connect(lambda: clear_highlights(self.buttons))

        self.highlight_timer = QTimer()
        self.highlight_timer.setSingleShot(True)
        self.highlight_active = False
        self.highlight_timer.timeout.connect(self.cancel_highlight)

        self.pulse_timer = QTimer(self)
        self.pulse_timer.setInterval(500)
        self.pulse_timer.timeout.connect(self._toggle_pulse)
        self.pulse_state = False

        print("[WEN INIT] Layout setup complete.")

    def set_branding_icon(self, icon_name="WEN_flow_Logo.ico"):
        if self.theme_mgr:
            icon_path = self.theme_mgr.get_icon_path(icon_name)
            print(f"[DEBUG] Setting branding icon: {icon_path}")
            self.setWindowIcon(QIcon(icon_path))

    def _toggle_pulse(self):
        pass

    def cancel_highlight(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = WENPalette(get_data_path("WEN_palette_runtime_layout_default.json"))
    theme_mgr = ThemeManager(app, window)
    window.theme_mgr = theme_mgr
    window.set_branding_icon()
    theme_mgr.load_theme("dark")

    window.show()
    QTimer.singleShot(18000, app.quit)
    sys.exit(app.exec())
