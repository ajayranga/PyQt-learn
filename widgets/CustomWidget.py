from random import randint
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel


class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Widget")

        layout = QVBoxLayout()
        label = QLabel("Custom Widget %d" % randint(0, 30))

        layout.addWidget(label)
        self.setLayout(layout)
