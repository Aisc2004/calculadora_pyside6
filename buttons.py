from PySide6.QtWidgets import QPushButton, QGridLayout
import re
from PySide6.QtCore import Slot
from display import Display
from info import Info

class Button(QPushButton):
    """
    Inicializa a função botão 
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config()

    def config(self):
        ...
        
class ButtonGrid(QGridLayout):
    """
    Classe que faz a formatação em grid dos botões
    """
    def __init__(self, display : Display, info: Info , *args, **kwargs ):
        super().__init__(*args, **kwargs)

        self._list_buttons = [
            ['C', 'DEL', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self._equation = ''
        self._make_button()

        @property
        def equation(self):
            return self._equation
        
        @equation.setter
        def equation(self, value):
            self._equation = value
            self.info.setText(value)

    
    def is_numeric_or_dot(self, string):
        """
        utilizando expressão regular para checar o intervalo de numéros e o ponto, a
        função recebe uma string e retorna o booleano 
        """
        num_or_dot = re.compile(r'^[0-9.]$')
        return bool(num_or_dot.search(string))
    
    def valid_number(self, string):
        valid = False
        try:
            float(string)
            valid = True
        except:
            valid = False
        return valid
    
    def _make_button(self):
        """
        desempacotamento de _list_buttons e adicionando os caracteres nos botões.
        Se a função is_numeric retornar False, é um caractere especial e vai receber um 
        style diferente. 
        """

        for i, row in enumerate(self._list_buttons):
            for j, button_text in enumerate(row):
                button = Button(button_text)
                self.addWidget(button , i, j)

                if not self.is_numeric_or_dot(button_text):
                    button.setObjectName("operacoes")
        
                button_slot = self._make_button_display_slot(
                    self._insert_text_in_button, button
                )
                button.clicked.connect(button_slot)

    def _make_button_display_slot(self, func, *args, **kwargs):
        @Slot()
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    def _insert_text_in_button(self, button):
        button_text = button.text()
        value_new_display = self.display.text() + button_text

        if not self.valid_number(value_new_display):
            return
        
        self.display.insert(button_text)



