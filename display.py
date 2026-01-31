from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QKeyEvent
from variables import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH, is_numeric_or_dot

class Display(QLineEdit):
    eq_request = Signal()
    del_request = Signal()
    clear_request = Signal()
    input_request = Signal(str)
    input_operator = Signal(str)

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
        action = event.text()
        key = event.key()
               
        KEYS = Qt.Key
        is_enter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        is_delete = key in [KEYS.Key_Backspace, KEYS.Key_Delete]
        is_escape = key in [KEYS.Key_Escape]  
        is_operator = key in [KEYS.Key_Plus, KEYS.Key_Minus, KEYS.Key_Slash, KEYS.Key_Asterisk, KEYS.Key_P]

        if is_enter or action == '=':
            self.eq_request.emit()
            return event.ignore()
        
        if is_operator:
            if action.lower() == 'p':
                action = '^'
            self.input_operator.emit(action)
            return event.ignore()

        if is_delete or action.upper() == 'D':
            self.del_request.emit()
            return event.ignore()
        
        if is_escape or action.upper() == 'C' :
            self.clear_request.emit()
            return event.ignore()

        if len(action) == 0:
            return event.ignore()
                
        if is_numeric_or_dot(action):
            self.input_request.emit(action)
            return event.ignore()

        
        return super().keyPressEvent(event)


