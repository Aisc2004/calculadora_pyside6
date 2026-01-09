import sys
from display import Display
from info import Info
from buttons import Button, ButtonGrid
from PySide6.QtCore import Slot
from PySide6.QtWidgets import  QMainWindow, QWidget,  QVBoxLayout

class MainWindows(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.setWindowTitle('Calculadora')
        self.layout = QVBoxLayout()
        self.main_widget.setLayout(self.layout)
        
        info = Info('visulização da conta')
        self.add_layout(info)

        display = Display()
        self.add_layout(display)

        button_grid = ButtonGrid(display)
        self.layout.addLayout(button_grid)

    def add_layout(self, widget : QWidget):
        self.layout.addWidget(widget)

    def adjust_fixed_size(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

        


