from re import L
import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
    QListWidget,
    QScrollArea,
    QGroupBox,
    QFormLayout,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Widgets App")

        layout = QVBoxLayout()
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]

        # for w in widgets:
        #     layout.addWidget(w())

        self.label = QLabel()
        self.label.setPixmap(QPixmap("assets/otje.webp"))
        self.label.setScaledContents(True)
        self.label.setToolTip("This is a cat")

        self.label2 = QLabel("Hello")
        self.label2.setScaledContents(True)
        self.label2.setToolTip("Empty")
        # self.label.setMinimumHeight(200)

        self.checkBox = QCheckBox("Not Checked")
        self.checkBox.setTristate(True)
        self.checkBox.stateChanged.connect(self.handle_checkbox_checked)

        comboBox = QComboBox()
        comboBox.addItems(["One", "Two", "Three"])
        comboBox.setCurrentIndex(-1)
        comboBox.setEditable(True)
        comboBox.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)
        comboBox.currentTextChanged.connect(self.handle_combobox_text_change)

        listWidget = QListWidget()
        listWidget.addItems(["One", "Two", "Three"])
        listWidget.currentTextChanged.connect(self.handle_listWidget_text_change)

        input = QLineEdit()
        input.setMaxLength(20)
        input.setPlaceholderText("Enter your text")
        input.returnPressed.connect(self.return_pressed)
        input.selectionChanged.connect(self.selection_changed)
        input.textChanged.connect(self.text_changed)
        input.textEdited.connect(self.text_edited)

        spinBox = QSpinBox()
        spinBox.setMaximum(5)
        spinBox.setMinimum(-5)
        spinBox.setPrefix("$")
        spinBox.setSuffix("c")
        spinBox.setSingleStep(1)

        spinBoxDouble = QDoubleSpinBox()
        spinBoxDouble.setMaximum(5)
        spinBoxDouble.setMinimum(-5)
        spinBoxDouble.setPrefix("$")
        spinBoxDouble.setSuffix("c")
        spinBoxDouble.setSingleStep(1)

        slider = QSlider()
        slider.setMaximum(5)
        slider.setMinimum(-5)
        slider.setSingleStep(1)
        slider.setOrientation(Qt.Orientation.Horizontal)
        slider.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        slider.setMinimumHeight(100)

        dial = QDial()
        dial.setRange(-20, 50)
        dial.setSingleStep(1)
        dial.setOrientation(Qt.Orientation.Horizontal)
        dial.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        dial.setMinimumHeight(100)
        dial.valueChanged.connect(self.dial_value_changed)

        layout.addWidget(self.label)
        layout.addWidget(self.label2)
        layout.addWidget(self.checkBox)
        layout.addWidget(comboBox)
        layout.addWidget(listWidget)
        layout.addWidget(input)
        layout.addWidget(spinBox)
        layout.addWidget(spinBoxDouble)
        layout.addWidget(slider)
        layout.addWidget(dial)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        self.setMinimumSize(QSize(480, 320))

    def handle_checkbox_checked(self, checked):
        if checked == 2:
            self.checkBox.setText("Checked")
        elif checked == 1:
            self.checkBox.setText("Partially Checked")
        else:
            self.checkBox.setText("Not Checked")

    def handle_combobox_text_change(self, txt):
        print(txt)

    def handle_listWidget_text_change(self, txt):
        print(txt)

    def return_pressed(self):
        print("Return pressed!")
        self.label.setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.label.selectedText())

    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s)

    def dial_value_changed(self, d):
        self.label2.setText(str(d))


def main():
    app = QApplication(sys.argv)
    docker = MainWindow()
    docker.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
