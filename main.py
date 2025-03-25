import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QHBoxLayout
from PyQt5.QtCore import QSize
from widgets.Color import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Docker")

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(Color("green"))
        vertical_layout.addWidget(Color("white"))
        vertical_layout.addWidget(Color("blue"))
        vertical_layout.addWidget(Color("teal"))

        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(Color("white"))
        horizontal_layout.addWidget(Color("green"))
        horizontal_layout.addWidget(Color("blue"))
        horizontal_layout.addWidget(Color("teal"))

        vertical_layout.addLayout(horizontal_layout)
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        vertical_layout.setSpacing(0)
        horizontal_layout.setSpacing(0)
        horizontal_layout.setContentsMargins(0, 5, 0, 0)

        container = QWidget()
        container.setLayout(vertical_layout)

        self.setCentralWidget(container)
        self.setFixedSize(QSize(480, 320))


def main():
    app = QApplication(sys.argv)
    docker = MainWindow()
    docker.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
