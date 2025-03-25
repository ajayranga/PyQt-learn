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

        label = QLabel("Label")
        label.setStatusTip("Label")
        label.setAlignment(Qt.AlignCenter)

        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        toolbar.setMovable(True)
        toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        button_action1 = QAction(
            QIcon("assets/icons/icons/bug.png"), "Bug Button", self
        )
        button_action1.setStatusTip("Bug btn")
        button_action1.setShortcut(QKeySequence("Ctrl+p"))
        button_action1.setCheckable(True)
        button_action1.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action1)

        button_action2 = QAction(
            QIcon("assets/icons/icons/diamond.png"), "Diamond Button", self
        )
        button_action2.setStatusTip("Diamond btn")
        button_action2.setCheckable(True)
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action2)

        self.setStatusBar(QStatusBar(self))

        self.addToolBar(toolbar)

        menu = self.menuBar()
        filemanu = menu.addMenu("&File")
        filemanu.addAction(button_action1)
        filemanu.addSeparator()

        file_submanu = filemanu.addMenu("Submenu")
        file_submanu.addAction(button_action2)
        file_submanu.addSeparator()

        self.setCentralWidget(label)
        self.setMinimumSize(QSize(480, 320))

    def onMyToolBarButtonClick(self, s):
        print("Clicked ", s)


def main():
    app = QApplication(sys.argv)
    docker = MainWindow()
    docker.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
