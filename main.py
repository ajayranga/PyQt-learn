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
    QMessageBox,
)
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import Qt, QSize
from widgets.Color import Color
from widgets.CustomDialog import CustomDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Docker")

        horizontal_layout = QHBoxLayout()

        button = QPushButton("Button")
        button.setStatusTip("Button")
        button.setFixedSize(QSize(80, 40))
        button.setCheckable(True)
        button.clicked.connect(self.handle_btn_click)

        button2 = QPushButton("Button2")
        button2.setStatusTip("Button2")
        button2.setFixedSize(QSize(80, 40))
        button2.setCheckable(True)
        button2.clicked.connect(self.handle_btn_click2)

        horizontal_layout.addWidget(button)
        horizontal_layout.addWidget(button2)

        container = QWidget()
        container.setLayout(horizontal_layout)

        self.statusBar()
        self.setCentralWidget(container)
        self.setMinimumSize(QSize(480, 320))

    def handle_btn_click(self, s):
        dlg = CustomDialog(parent=self)
        res = dlg.exec()
        print("res", res)

    def handle_btn_click2(self, s):
        button = QMessageBox.critical(
            self,
            "Oh dear!",
            "Something went very wrong.",
            buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
            defaultButton=QMessageBox.Discard,
        )

        if button == QMessageBox.Discard:
            print("Discard!")
        elif button == QMessageBox.NoToAll:
            print("No to all!")
        else:
            print("Ignore!")


def main():
    app = QApplication(sys.argv)
    docker = MainWindow()
    docker.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
