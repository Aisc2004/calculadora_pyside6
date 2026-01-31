import re

#sizing
BIG_FONT_SIZE = 40
MEDIUM_FONT_SIZE = 24
SMALL_FONT_SIZE = 18
TEXT_MARGIN = 15
MINIMUM_WIDTH = 500

#colors
WHITE_COLOR = '#ffffff'
PRIMARY_COLOR = '#a167c9'
SECUNDARY_COLOR = '#640ba7'
TERCIARY_COLOR = '#410287'

def is_numeric_or_dot(action):
    """
    utilizando expressão regular para checar o intervalo de numéros e o ponto, a
    função recebe uma string e retorna o booleano 
    """
    num_or_dot = re.compile(r'^[0-9.]$')
    return bool(num_or_dot.search(action))