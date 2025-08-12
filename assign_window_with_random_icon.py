
import os
import random
from PySide6.QtGui import QIcon

def get_unused_icon(existing_icons, icon_folder="resources"):
    all_icons = [f for f in os.listdir(icon_folder) if f.endswith(".ico")]
    unused = list(set(all_icons) - set(existing_icons))
    if not unused:
        print("[INFO] All icons are used.")
        return None
    return random.choice(unused)



def assign_window(self, btn):
    if not self.highlight_active:
        print("Use the '+' button to associate a window with this button.")
        return

    print(f">> Assigning window to: {btn.slot_id}")

    used_icons = [v.get("icon", "") for v in self.layout_data.values() if isinstance(v, dict)]
    random_icon = get_unused_icon(used_icons)

    icon_path = os.path.join("resources", random_icon) if random_icon else "resources/default.ico"

    assigned_app = {
        "name": "ExampleApp",
        "exe_path": "C:/Path/To/ExampleApp.exe",
        "icon": random_icon,
        "tooltip": "ExampleApp"
    }

    btn.setProperty("class", "assigned")
    btn.setToolTip(assigned_app["tooltip"])
    btn.setText("")
    btn.setIcon(QIcon(icon_path))
    btn.setIconSize(btn.size())

    self.layout_data[btn.slot_id] = assigned_app

    btn.style().unpolish(btn)
    btn.style().polish(btn)

    self._deactivate_highlight()
