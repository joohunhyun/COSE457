from model.object import Object
from PyQt5.QtGui import QColor

class RectangleObject(Object):
    def __init__(self, id, x, y, width, height, z_order, fill_color=QColor("white"), stroke_color=QColor("black")):
        super().__init__(id, "rectangle", z_order)
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._fill_color = fill_color
        self._stroke_color = stroke_color

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        self.property_changed.emit("x", value)

    # Similar properties for y, width, height, fill_color, stroke_color