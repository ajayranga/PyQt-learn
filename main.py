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
    QMainWindow,
    QApplication,
    QLabel,
    QToolBar,
    QAction,
    QDialog,
    QStatusBar,
)
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import Qt, QSize
from widgets.Color import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Docker")

        button = QPushButton("Button")
        button.setStatusTip("Button")
        button.setFixedSize(QSize(80, 40))
        button.clicked.connect(self.handle_btn_click)

        self.setCentralWidget(button)
        self.setMinimumSize(QSize(480, 320))

    def handle_btn_click(self, s):
        print("Clicked ", s)
        dlg = QDialog(self)
        dlg.setWindowTitle("Dialog cc")
        dlg.setFixedSize(QSize(180, 140))

        dlg.show()


def main():
    app = QApplication(sys.argv)
    docker = MainWindow()
    docker.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
