from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PyQt5.QtGui import QColor

class ColorPalette(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        colors = [QColor("red"), QColor("green"), QColor("blue"), QColor("yellow"), QColor("black")]
        for color in colors:
            btn = QPushButton()
            btn.setStyleSheet(f"background-color: {color.name()}")
            btn.clicked.connect(lambda checked, c=color: self.apply_color(c))
            self.layout.addWidget(btn)

    def apply_color(self, color):
        # This will be connected to the controller to apply the color to selected objects
        pass