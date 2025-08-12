from PySide6.QtWidgets import QApplication, QWidget, QDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import sys

def load_ui(file_path):
    loader = QUiLoader()
    ui_file = QFile(file_path)
    ui_file.open(QFile.ReadOnly)
    window = loader.load(ui_file)
    ui_file.close()
    return window

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Load main palette
    palette = load_ui("ui/wen_palette.ui")
    palette.show()

    # Wire Chrome Manager
    def open_chrome_manager():
        chrome_mgr = load_ui("ui/chrome_manager.ui")
        chrome_mgr.exec()

    palette.findChild(QWidget, "chromeButton").clicked.connect(open_chrome_manager)

    sys.exit(app.exec())
