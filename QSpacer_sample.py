from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QSpacerItem, QSizePolicy,QWidget

app = QApplication([])
window = QMainWindow()
layout = QGridLayout()
window.setCentralWidget(QWidget())
window.centralWidget().setLayout(layout)

# Add buttons with spacers
for i in range(4):
    print(f"Adding button {i+1}")
    btn = QPushButton(f"Btn {i+1}")
    btn.setFixedSize(40, 40)
    layout.addWidget(btn, 0, i * 2, 1, 1)  # Every other column
    if i < 3:  # Add spacer between buttons
        print(f"Adding spacer after button {i+1}")
        spacer = QSpacerItem(10, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)
        layout.addItem(spacer, 0, i * 2 + 1, 1, 1)  # Spacer in between

window.setFixedSize(350, 100)
window.show()
app.exec()