
# --- highlight_manager.py (New Module) ---

from PySide6.QtCore import QTimer

class HighlightManager:
    def __init__(self, button_group, class_name, timeout_ms=10000):
        self.button_group = button_group
        self.class_name = class_name
        self.timeout_ms = timeout_ms
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.clear_highlights)

    def toggle_highlights(self):
        if self.is_highlight_active():
            self.clear_highlights()
        else:
            self.set_highlights()

    def is_highlight_active(self):
        return any(b.property("class") == self.class_name for b in self.button_group)

    def set_highlights(self):
        for b in self.button_group:
            if b.property("class") == self.class_name:
                continue
            b.setProperty("class", self.class_name)
            b.style().unpolish(b)
            b.style().polish(b)
        self.timer.start(self.timeout_ms)

    def clear_highlights(self):
        for b in self.button_group:
            if b.property("class") == self.class_name:
                b.setProperty("class", "")
                b.style().unpolish(b)
                b.style().polish(b)
        self.timer.stop()
