from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from display import Display
from info import Info
import re

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
    def __init__(self, display : Display, info: Info , window,  *args, **kwargs ):
        super().__init__(*args, **kwargs)

        self._list_buttons = [
            ['C', 'D', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '='],
        ]
        self.display = display
        self.info = info
        self.window = window
        self._equation = ''
        self.left = None
        self.right = None
        self.operator = None

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
            if float(string) or string == '-':
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
        self.display.eq_request.connect(self._equality)
        self.display.del_request.connect(self._backspace)
        self.display.clear_request.connect(self._clear)
        self.display.input_request.connect(self._insert_text_in_button)
        self.display.input_operator.connect(self._operator_clicked)

        for i, row in enumerate(self._list_buttons):
            for j, button_text in enumerate(row):
                button = Button(button_text)

                if button_text == '0':
                    self.addWidget(button, i, j, 1, 2) 
                elif i == 4 and j > 0:
                    self.addWidget(button, i, j + 1)
                else:
                    self.addWidget(button, i, j)

                if self.is_numeric_or_dot(button_text):
                    button_slot = self._make_button_display_slot(
                    self._insert_text_in_button, button_text
                )
                    self._connect_button_clicked(button, button_slot)
                else:
                    button.setObjectName("operacoes")
                    self._config_special_button(button)

    def _connect_button_clicked(self, button, button_slot):
        button.clicked.connect(button_slot)

    def _make_button_display_slot(self, func, *args, **kwargs):
        @Slot()
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot
    
    def _config_special_button(self, button):
        text = button.text()

        if text == 'C':
            self._connect_button_clicked(button, self._clear)

        if text == 'D':
            self._connect_button_clicked(button, self.display.backspace)

        if text in '+-/*^':
            self._connect_button_clicked(
                button, self._make_button_display_slot(self._operator_clicked, text)
            )

        if text == '=':
            self._connect_button_clicked(
                button, self._equality)

    @Slot()
    def _insert_text_in_button(self, text):
        value_new_display = self.display.text() + text

        if not self.valid_number(value_new_display) and text not in '+-=*/^':
            return
        
        self.display.insert(text)
        self.display.setFocus()

    @Slot()
    def _clear(self):
        self.left = None
        self.right = None
        self.operator = None
        self.equation = ''
        self.display.clear()
        self.display.setFocus()

    @Slot()
    def _operator_clicked(self, text):
        display_text = self.display.text()

        if not self.valid_number(display_text):
            if text == '-' and display_text == '':
                self.display.insert(text)
                return
            self._showError('Coloque um número')
            return
        
        if self.left is None:
            self.left = float(display_text)

        self.operator = text
        self.equation = f'{self.left} {self.operator}'
        self.display.clear()
        self.display.setFocus()

    @Slot()
    def _equality(self):
        display_text = self.display.text()

        if not self.valid_number(display_text) or self.operator is None:
            return
        
        
        self.right = float(display_text)

        self.equation = f'{self.left} {self.operator} {self.right}'

        result = 'error'

        try:
            if self.operator == '^':
                result = self.left ** self.right
            else:
                result = eval(self.equation)

            self.display.setText(str(result))
            self.info.setText(f'{self.equation} = {result}')
            self.left = result
            self.right = None
            self.operator = None
            self.display.setFocus()
        
        except ZeroDivisionError:
            self._showError('Divisão por zero')

        except OverflowError:
             self._showError('Overflow')
    @Slot()
    def _backspace(self):
        self.display.backspace()
        self.display.setFocus()

    def _makeDialog(self, text):
        msgBox = self.window.make_msg_box()
        msgBox.setText(text)
        return msgBox

    def _showError(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.exec()
        self.display.setFocus()