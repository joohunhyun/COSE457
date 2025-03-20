from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QLabel
from PyQt5.QtGui import QColor

class PropertiesPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QFormLayout()
        self.setLayout(self.layout)

    def update_properties(self, objects):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)
        if not objects:
            return  # Show nothing when no object selected
        elif len(objects) > 1:
            self.layout.addRow(QLabel("Multiple objects selected"))
        else:
            obj = objects[0]
            if obj.type == "rectangle":
                self.layout.addRow("X:", QLineEdit(str(obj.x)))
                self.layout.addRow("Y:", QLineEdit(str(obj.y)))
                self.layout.addRow("Width:", QLineEdit(str(obj.width)))
                self.layout.addRow("Height:", QLineEdit(str(obj.height)))
                # Add color pickers for fill_color, stroke_color