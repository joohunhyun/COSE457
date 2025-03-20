from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt5.QtCore import Qt

class CanvasView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.setSceneRect(0, 0, 800, 600)

    def add_object(self, obj):
        # Create QGraphicsItem based on obj.type and properties
        # Add to scene with obj.z_order
        pass

    def update_object(self, obj, property_name, value):
        # Update corresponding QGraphicsItem
        pass