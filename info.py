from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QWidget
from variables import SMALL_FONT_SIZE

class Info(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_style()

    def config_style(self):
        self.setStyleSheet(f'font-size {SMALL_FONT_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)