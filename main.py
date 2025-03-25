import sys
from PyQt5.QtWidgets import (
    QMainWindow,
    QGridLayout,
    QApplication,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
    QStackedLayout,
    QTabWidget,
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

        tabs = QTabWidget()
        tabs.setMovable(True)
        tabs.setDocumentMode(True)
        for n, color in enumerate(["red", "green", "yellow"]):
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)
        self.setFixedSize(QSize(480, 320))


def main():
    app = QApplication(sys.argv)
    docker = MainWindow()
    docker.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
