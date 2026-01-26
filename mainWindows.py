import sys
from display import Display
from info import Info
from buttons import ButtonGrid
from PySide6.QtWidgets import  QMainWindow, QWidget,  QVBoxLayout, QMessageBox

class MainWindows(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.setWindowTitle('Calculadora')
        self.layout = QVBoxLayout()
        self.main_widget.setLayout(self.layout)
        
        self.info = Info('r')
        self.add_layout(self.info)

        self.display = Display()
        self.add_layout(self.display)

        button_grid = ButtonGrid(self.display, self.info, self)
        self.layout.addLayout(button_grid)
    
    def add_layout(self, widget : QWidget):
        self.layout.addWidget(widget)

    def adjust_fixed_size(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def make_msg_box(self):
        msg_box =  QMessageBox(self)
        return msg_box

        


