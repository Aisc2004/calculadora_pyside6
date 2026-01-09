import sys
from mainWindows import MainWindows
from PySide6.QtWidgets import QApplication
from style import setup_theme

if __name__ == '__main__':
    app = QApplication(sys.argv)
    setup_theme(app)
    windows = MainWindows()
    windows.show()
    
    windows.adjust_fixed_size()
    app.exec()