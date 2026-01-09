from variables import PRIMARY_COLOR, SECUNDARY_COLOR, TERCIARY_COLOR
from qt_material import apply_stylesheet
    
def setup_theme(app):

    apply_stylesheet(app, theme='dark_purple.xml')

    style_button = f"""
        Button[class="button"] {{
            color: {PRIMARY_COLOR};
            border radius: 5px;
            font-size: 15px;
            font-weight: bold;
            min-width: 75;
            min-height: 75;
        }}

        Button:hover{{
            color: {TERCIARY_COLOR};
        }}

        Button:pressed{{
            color: {SECUNDARY_COLOR}
        }}
"""

    existing_stylesheet = app.styleSheet()
    app.setStyleSheet(existing_stylesheet + style_button)

    
