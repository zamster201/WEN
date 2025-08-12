
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

class ThemeManager:
    def __init__(self, app, palette_window):
        self.app = app
        self.window = palette_window
        self.current_theme = "dark"
        self.theme_paths = {
            "dark": "wen/core/dark_theme_wen.qss",
             "light": "wen/core/light_theme.qss"
        }
        self.theme_icons = {
            "dark": "sun.ico",
            "light": "moon.ico"
        }

    def load_theme(self, theme_name):
        qss_path = self.theme_paths.get(theme_name)
        if qss_path:
            try:
                with open(qss_path, "r", encoding="utf-8") as f:
                    self.app.setStyleSheet(f.read())
                self.current_theme = theme_name
                self.update_theme_button_icon()
            except Exception as e:
                print(f"Failed to load theme '{theme_name}':", e)

    def toggle_theme(self):
        new_theme = "light" if self.current_theme == "dark" else "dark"
        self.load_theme(new_theme)

    def update_theme_button_icon(self):
        for btn in self.window.buttons:
            if getattr(btn, 'slot_id', '') == "Theme_Toggle":
                icon_path = self.theme_icons.get(self.current_theme)
                if icon_path:
                    btn.setIcon(QIcon(icon_path))
