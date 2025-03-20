from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QAction
from PyQt5.QtCore import Qt
from view.canvas_view import CanvasView
from view.properties_panel import PropertiesPanel
from view.toolbar import Toolbar
from view.color_palette import ColorPalette

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vector Graphics Editor")
        self.setGeometry(100, 100, 1200, 800)  # Set window size for better visibility

        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout(central_widget)

        # Create UI components
        self.toolbar = Toolbar()
        self.canvas_view = CanvasView()
        self.properties_panel = PropertiesPanel()
        self.color_palette = ColorPalette()

        # Create a vertical layout for the canvas and color palette
        canvas_and_palette_layout = QVBoxLayout()
        canvas_and_palette_layout.addWidget(self.canvas_view, 4)  # Canvas takes more space
        canvas_and_palette_layout.addWidget(self.color_palette, 1)  # Color palette at the bottom

        # Add components to the main horizontal layout
        layout.addWidget(self.toolbar, 1)  # Left toolbar
        layout.addLayout(canvas_and_palette_layout, 4)  # Center canvas + color palette
        layout.addWidget(self.properties_panel, 1)  # Right properties panel

        # Add menu bar with File, Edit, Object, View
        self.setup_menu_bar()

    def setup_menu_bar(self):
        menu_bar = self.menuBar()
        menu_bar.addMenu("File")
        menu_bar.addMenu("Edit")
        object_menu = menu_bar.addMenu("Object")
        menu_bar.addMenu("View")

        # Add z-order actions to the Object menu
        bring_to_front = QAction("Bring to Front", self)
        send_to_back = QAction("Send to Back", self)
        object_menu.addAction(bring_to_front)
        object_menu.addAction(send_to_back)

        # Connect actions to controller methods
        bring_to_front.triggered.connect(lambda: self.canvas_view.controller.bring_to_front_selected())
        send_to_back.triggered.connect(lambda: self.canvas_view.controller.send_to_back_selected())