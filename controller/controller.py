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
        }
        self.current_tool = self.tools["select"]

        # Connect signals
        self.model.object_added.connect(self.view.canvas_view.add_object)
        self.model.selection_changed.connect(self.view.properties_panel.update_properties)
        self.view.canvas_view.set_controller(self)

        # Connect toolbar buttons
        self.view.toolbar.select_btn.clicked.connect(lambda: self.set_tool("select"))
        self.view.toolbar.rectangle_btn.clicked.connect(lambda: self.set_tool("rectangle"))

    def set_tool(self, tool_name):
        self.current_tool = self.tools[tool_name]

    def bring_to_front_selected(self):
        for obj in self.model.selected_objects:
            self.model.bring_to_front(obj)

    def send_to_back_selected(self):
        for obj in self.model.selected_objects:
            self.model.send_to_back(obj)