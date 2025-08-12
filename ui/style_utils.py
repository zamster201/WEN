# wen/ui/style_utils.py
from PySide6.QtWidgets import QWidget
from wen.config.theme import THEME

def apply_theme(widget: QWidget, theme_mode="dark"):
    theme = THEME["colors"][theme_mode]
    font = THEME["fonts"]["primary"]
    
    widget.setStyleSheet(f"""
        background-color: {theme['background']};
        color: {theme['text']};
        font-family: {font};
        font-size: {THEME['fonts']['size']}pt;
    """)
