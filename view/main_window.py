from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from view.canvas_view import CanvasView
from view.properties_panel import PropertiesPanel
from view.toolbar import Toolbar
from view.color_palette import ColorPalette

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vector Graphics Editor")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout(central_widget)

        self.toolbar = Toolbar()
        self.canvas_view = CanvasView()
        self.properties_panel = PropertiesPanel()
        self.color_palette = ColorPalette()

        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas_view)
        layout.addWidget(self.properties_panel)
        layout.addWidget(self.color_palette, alignment="bottom")

        # Add menu bar with File, Edit, Object, View
        menu_bar = self.menuBar()
        menu_bar.addMenu("File")
        menu_bar.addMenu("Edit")
        menu_bar.addMenu("Object")
        menu_bar.addMenu("View")