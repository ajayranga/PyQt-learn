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
from widgets.CustomWidget import CustomWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.widget1 = CustomWidget()
        self.widget2 = CustomWidget()
        # self.show_widget = False

    def setup_ui(self):
        self.setWindowTitle("Docker")

        horizontal_layout = QHBoxLayout()

        self.button = QPushButton("Open Widget")
        self.button.setStatusTip("Open Widget")
        self.button.setFixedSize(QSize(120, 40))
        self.button.setCheckable(True)
        self.button.clicked.connect(
            lambda checked: self.handle_btn_click(self.widget1, self.button)
        )

        horizontal_layout.addWidget(self.button)

        self.button2 = QPushButton("Open Widget")
        self.button2.setStatusTip("Open Widget")
        self.button2.setFixedSize(QSize(120, 40))
        self.button2.setCheckable(True)
        self.button2.clicked.connect(
            lambda checked: self.handle_btn_click(self.widget2, self.button2)
        )

        horizontal_layout.addWidget(self.button2)

        container = QWidget()
        container.setLayout(horizontal_layout)

        self.statusBar()
        self.setCentralWidget(container)
        self.setMinimumSize(QSize(480, 320))

    def handle_btn_click(self, widget, button):
        if widget.isVisible():
            widget.hide()
            button.setText("Open Widget")
        else:
            widget.show()
            button.setText("Hide Widget")
        # if self.show_widget:
        #     self.widget.close()
        #     self.button.setText("Open Widget")
        # else:
        #     self.widget.show()
        #     self.button.setText("Hide Widget")
        # self.show_widget = not self.show_widget


def main():
    app = QApplication(sys.argv)
    docker = MainWindow()
    docker.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
