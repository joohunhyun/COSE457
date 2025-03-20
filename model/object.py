from PyQt5.QtCore import QObject, pyqtSignal

class Object(QObject):
    property_changed = pyqtSignal(str, object)

    def __init__(self, id, type, z_order):
        super().__init__()
        self.id = id
        self.type = type
        self._z_order = z_order

    @property
    def z_order(self):
        return self._z_order

    @z_order.setter
    def z_order(self, value):
        self._z_order = value
        self.property_changed.emit("z_order", value)