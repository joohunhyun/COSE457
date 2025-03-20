from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsRectItem
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPen, QBrush

class CanvasView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.setSceneRect(0, 0, 800, 600)
        self.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.controller = None
        self.items_map = {}  # Map model objects to QGraphicsItems

    def set_controller(self, controller):
        self.controller = controller

    def add_object(self, obj):
        if obj.type == "rectangle":
            item = QGraphicsRectItem(obj.x, obj.y, obj.width, obj.height)
            item.setPen(QPen(obj.stroke_color))
            item.setBrush(QBrush(obj.fill_color))
            item.setZValue(obj.z_order)
            item.setFlag(QGraphicsRectItem.ItemIsSelectable, True)
            item.setFlag(QGraphicsRectItem.ItemIsMovable, True)
            item.setData(0, obj)  # Store model object in item
            self.scene.addItem(item)
            self.items_map[obj] = item

        obj.property_changed.connect(self.update_object)

    def update_object(self, property_name, value):
        obj = self.sender()
        item = self.items_map.get(obj)
        if not item:
            return
        if property_name == "x":
            item.setX(value)
        elif property_name == "y":
            item.setY(value)
        elif property_name == "width" or property_name == "height":
            item.setRect(obj.x, obj.y, obj.width, obj.height)
        elif property_name == "fill_color":
            item.setBrush(QBrush(value))
        elif property_name == "stroke_color":
            item.setPen(QPen(value))
        elif property_name == "z_order":
            item.setZValue(value)

    def mousePressEvent(self, event):
        if self.controller:
            self.controller.current_tool.mouse_press(event)
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.controller:
            self.controller.current_tool.mouse_move(event)
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.controller:
            self.controller.current_tool.mouse_release(event)
        super().mouseReleaseEvent(event)