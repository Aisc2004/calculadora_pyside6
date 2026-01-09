from PySide6.QtWidgets import QPushButton


class Button(QPushButton):
    """
    Inicializa a função botão 
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config()

    def config(self):
        self.setProperty("class", "button")
        

    
