import sys
from PyQt5.QtWidgets import QApplication
from model.canvas import Canvas
from view.main_window import MainWindow
from controller.controller import Controller

if __name__ == "__main__":
    app = QApplication(sys.argv)
    model = Canvas()
    view = MainWindow()
    controller = Controller(model, view)
    view.show()
    sys.exit(app.exec_())