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

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
        self.property_changed.emit("y", value)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
        self.property_changed.emit("width", value)

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
        self.property_changed.emit("height", value)

    @property
    def fill_color(self):
        return self._fill_color

    @fill_color.setter
    def fill_color(self, value):
        self._fill_color = value
        self.property_changed.emit("fill_color", value)

    @property
    def stroke_color(self):
        return self._stroke_color

    @stroke_color.setter
    def stroke_color(self, value):
        self._stroke_color = value
        self.property_changed.emit("stroke_color", value)