from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QColor, QPalette


class Color(QWidget):

    def __init__(self, color: str):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)
