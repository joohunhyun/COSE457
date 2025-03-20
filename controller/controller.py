from model.factory import ObjectFactory
from controller.tools import SelectTool, RectangleTool

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.factory = ObjectFactory()
        self.tools = {
            "select": SelectTool(self),
            "rectangle": RectangleTool(self)
            # Add other tools
        }
        self.current_tool = self.tools["select"]

        # Connect signals
        self.model.object_added.connect(self.view.canvas_view.add_object)
        self.model.selection_changed.connect(self.view.properties_panel.update_properties)
        self.view.canvas_view.mousePressEvent = lambda event: self.current_tool.mouse_press(event)

    def set_tool(self, tool_name):
        self.current_tool = self.tools[tool_name]