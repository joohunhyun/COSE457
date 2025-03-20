from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

class Toolbar(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.select_btn = QPushButton("Select")
        self.rectangle_btn = QPushButton("Rectangle")

        self.layout.addWidget(self.select_btn)
        self.layout.addWidget(self.rectangle_btn)
        self.layout.addStretch()