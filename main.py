import sys
from PyQt5.QtWidgets import (
    QMainWindow,
    QGridLayout,
    QApplication,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
    QStackedLayout,
    QPushButton,
)
from PyQt5.QtCore import QSize
from widgets.Color import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Docker")

        vertical_layout = QVBoxLayout()
        horizontal_layout = QHBoxLayout()
        self.stacked_layout = QStackedLayout()

        vertical_layout.addLayout(horizontal_layout)
        vertical_layout.addLayout(self.stacked_layout)

        btn = QPushButton("red")
        btn.pressed.connect(self.activate_tab_1)
        horizontal_layout.addWidget(btn)
        self.stacked_layout.addWidget(Color("red"))

        btn = QPushButton("green")
        btn.pressed.connect(self.activate_tab_2)
        horizontal_layout.addWidget(btn)
        self.stacked_layout.addWidget(Color("green"))

        btn = QPushButton("yellow")
        btn.pressed.connect(self.activate_tab_3)
        horizontal_layout.addWidget(btn)
        self.stacked_layout.addWidget(Color("yellow"))

        container = QWidget()
        container.setLayout(vertical_layout)

        self.setCentralWidget(container)
        self.setFixedSize(QSize(480, 320))

    def activate_tab_1(self):
        self.stacked_layout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stacked_layout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stacked_layout.setCurrentIndex(2)


def main():
    app = QApplication(sys.argv)
    docker = MainWindow()
    docker.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
