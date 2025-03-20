from PyQt5.QtCore import QPointF

class Tool:
    def __init__(self, controller):
        self.controller = controller

    def mouse_press(self, event):
        pass

class SelectTool(Tool):
    def mouse_press(self, event):
        pos = event.pos()
        item = self.controller.view.canvas_view.itemAt(pos)
        if item:
            # Map item to model object and select
            self.controller.model.select_objects([item.data(0)])  # Assuming data(0) holds model object

class RectangleTool(Tool):
    def mouse_press(self, event):
        pos = event.pos()
        obj = self.controller.factory.create_object("rectangle", id=len(self.controller.model.objects),
                                                  x=pos.x(), y=pos.y())
        self.controller.model.add_object(obj)