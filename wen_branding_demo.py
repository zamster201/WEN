from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QFont, QColor, QPalette
from PySide6.QtCore import Qt

app = QApplication([])

window = QWidget()
window.setWindowTitle("WEN Branding Preview")
window.setFixedSize(480, 300)

# Apply WEN color palette
palette = QPalette()
palette.setColor(QPalette.Window, QColor("#1C1F26"))          # vapor_slate
palette.setColor(QPalette.Button, QColor("#C2C7CC"))          # window_silver
palette.setColor(QPalette.ButtonText, Qt.black)
palette.setColor(QPalette.WindowText, QColor("#00D1FF"))      # accent_cyan
palette.setColor(QPalette.Text, Qt.white)
app.setPalette(palette)

# Set global font
app.setFont(QFont("Inter", 12))

layout = QVBoxLayout()

title = QLabel("WEN Control Palette")
title.setFont(QFont("Poppins", 20, QFont.Bold))
title.setAlignment(Qt.AlignCenter)
title.setStyleSheet("color: #00D1FF")

btn_add = QPushButton("+  -  1  2  3  4  5  6  7  8  9 ")
btn_add.setStyleSheet("background-color: #FFA500; color: black;")

btn_save = QPushButton("Save  Open  Load   Close")
btn_save.setStyleSheet("background-color: #C2C7CC;")

btn_theme = QPushButton("🌙")
btn_theme.setStyleSheet("background-color: #C2C7CC; color: #1C1F26")

layout.addWidget(title)
layout.addWidget(btn_add)
layout.addWidget(btn_save)
layout.addWidget(btn_theme)
window.setLayout(layout)
window.show()

app.exec()
