from random import choice
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.button_is_checked = True

    window_titles = [
        "Docker",
        "My App Docker",
        "Still My App Docker",
        "Still My App Docker",
        "What on earth",
        "What on earth",
        "This is surprising",
        "This is surprising",
        "Something went wrong",
    ]

    def setup_ui(self):
        self.setWindowTitle("Docker")
        self.btn = QPushButton("Click Here")
        self.btn.setCheckable(True)
        self.btn.clicked.connect(self.on_btn_clicked)
        self.btn.clicked.connect(self.on_btn_toggled)
        self.btn.released.connect(self.on_btn_released)
        self.setCentralWidget(self.btn)
        self.setFixedSize(QSize(480, 320))

    def on_btn_clicked(self):
        # self.btn.setEnabled(False)
        print("Clicked")

    def on_btn_toggled(self, checked):
        if checked:
            self.btn.setText("Clicked")
        else:
            self.btn.setText("Click Here")
            self.setWindowTitle(choice(self.window_titles))
        print("Checked ", checked)

    def on_btn_released(self):
        self.button_is_checked = self.btn.isChecked()
        print("Released ")


def main():
    app = QApplication(sys.argv)
    docker = MainWindow()
    docker.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
