import sys
from PyQt5.uic import loadUi
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
    QMainWindow,
    QApplication,
    QLabel,
    QToolBar,
    QAction,
    QDialog,
    QStatusBar,
    QMessageBox,
)
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import Qt, QSize
from widgets.Color import Color
from widgets.CustomDialog import CustomDialog
from widgets.CustomWidget import CustomWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Docker")
        self.setup_ui()

    def setup_ui(self):
        self.window = loadUi("views/screen/mainwindow.ui", self)
        self.window.show()
        self.setMinimumSize(QSize(480, 320))


def main():
    app = QApplication(sys.argv)
    docker = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
