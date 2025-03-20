from PyQt5.QtCore import QPointF, Qt  # Added Qt import

class Tool:
    def __init__(self, controller):
        self.controller = controller

    def mouse_press(self, event):
        pass

    def mouse_move(self, event):
        pass

    def mouse_release(self, event):
        pass

class SelectTool(Tool):
    def mouse_press(self, event):
        pos = event.pos()
        item = self.controller.view.canvas_view.itemAt(pos)
        if item:
            obj = item.data(0)
            if event.modifiers() & Qt.ControlModifier:  # Now Qt is defined
                selected = self.controller.model.selected_objects.copy()
                if obj in selected:
                    selected.remove(obj)
                else:
                    selected.append(obj)
                self.controller.model.select_objects(selected)
            else:
                self.controller.model.select_objects([obj])
        else:
            self.controller.model.select_objects([])

class RectangleTool(Tool):
    def __init__(self, controller):
        super().__init__(controller)
        self.start_pos = None
        self.drawing = False

    def mouse_press(self, event):
        self.start_pos = self.controller.view.canvas_view.mapToScene(event.pos())
        self.drawing = True

    def mouse_move(self, event):
        if self.drawing:
            # Optional: You can add a preview of the rectangle while dragging
            pass

    def mouse_release(self, event):
        if self.drawing and self.start_pos:
            end_pos = self.controller.view.canvas_view.mapToScene(event.pos())
            x = min(self.start_pos.x(), end_pos.x())
            y = min(self.start_pos.y(), end_pos.y())
            width = abs(self.start_pos.x() - end_pos.x())
            height = abs(self.start_pos.y() - end_pos.y())

            # Create a new RectangleObject
            obj = self.controller.factory.create_object(
                "rectangle",
                id=len(self.controller.model.objects),
                x=x,
                y=y,
                width=width,
                height=height,
                z_order=len(self.controller.model.objects)
            )
            self.controller.model.add_object(obj)

            # Reset drawing state
            self.drawing = False
            self.start_pos = None