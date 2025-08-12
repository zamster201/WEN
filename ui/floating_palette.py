from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication
from wen import actions
import os

class FloatingPalette(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("WEN Control Panel")
        self.setMinimumSize(300, 200)

        icon_path = os.path.join(os.path.dirname(__file__), "..", "resources", "WEN_flow_logo.ico")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                color: white;
                font-size: 14px;
            }
            QPushButton {
                margin: 6px;
                padding: 6px;
                background-color: #222;
                border: 1px solid #00CCCC;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #333;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)

        btn1 = QPushButton("Launch App")
        btn1.clicked.connect(actions.launch_app)
        layout.addWidget(btn1)

        btn2 = QPushButton("Move Window")
        btn2.clicked.connect(actions.move_window)
        layout.addWidget(btn2)

        btn3 = QPushButton("Toggle Profile")
        btn3.clicked.connect(actions.toggle_profile)
        layout.addWidget(btn3)

        btn_quit = QPushButton("Quit WEN")
        btn_quit.clicked.connect(QApplication.quit)
        layout.addWidget(btn_quit)
