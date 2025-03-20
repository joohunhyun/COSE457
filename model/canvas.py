from PyQt5.QtCore import QObject, pyqtSignal
from model.object import Object

class Canvas(QObject):
    object_added = pyqtSignal(Object)
    object_removed = pyqtSignal(Object)
    selection_changed = pyqtSignal(list)

    def __init__(self, width=800, height=600):
        super().__init__()
        self._width = width
        self._height = height
        self.objects = []
        self.selected_objects = []

    def add_object(self, obj):
        self.objects.append(obj)
        self.object_added.emit(obj)

    def select_objects(self, objects):
        self.selected_objects = objects
        self.selection_changed.emit(objects)