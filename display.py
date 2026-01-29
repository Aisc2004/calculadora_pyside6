from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QKeyEvent
from variables import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH

class Display(QLineEdit):
    eqRequest = Signal()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_style()

    def config_style(self):
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(TEXT_MARGIN, TEXT_MARGIN, TEXT_MARGIN, TEXT_MARGIN)
        self.setPlaceholderText('Digite')
    
    def keyPressEvent(self, event: QKeyEvent) -> None:

        key = event.key()
               
        KEYS = Qt.Key

        if key == KEYS.Key_Enter or key == KEYS.Key_Return:
            print("enter")

        return super().keyPressEvent(event)
