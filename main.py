from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
import sys


class Docker(QMainWindow):
    def __init__(self, ):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        window = QWidget(self)
        window.show()


def main():
    app = QApplication(sys.argv)
    docker = Docker()
    docker.show()
    app.exec()


if __name__ == "__main__":
    main()
