from random import choice
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QLabel,
    QVBoxLayout,
    QLineEdit,
    QMenu,
)
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt, QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Docker")
        self.label = QLabel("Default Text")
        self.setMouseTracking(True)
        self.input = QLineEdit("Hello")
        self.input.textChanged.connect(self.label.setText)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.setFixedSize(QSize(480, 320))

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseReleaseEvent LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseReleaseEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseReleaseEvent RIGHT")

    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseDoubleClickEvent LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseDoubleClickEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseDoubleClickEvent RIGHT")

    def contextMenuEvent(self, event):
        # return super().contextMenuEvent(event)
        context = QMenu(self)
        context.addAction(QAction("Hello", self))
        context.addAction(QAction("Hello 1", self))
        context.addAction(QAction("Hello 2", self))
        context.exec(event.globalPos())


def main():
    app = QApplication(sys.argv)
    docker = MainWindow()
    docker.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
