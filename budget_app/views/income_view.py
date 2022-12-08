import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QLineEdit,
    QVBoxLayout,
    QLabel,
)

# WINDOW_SIZE = 235
# DISPLAY_HEIGHT = 35
# BUTTON_SIZE = 40
# ERROR_MSG = "ERROR"


class IncomeView(QVBoxLayout):
    """Class to represent Income"""

    def __init__(self, parent=None):
        super(IncomeView, self).__init__(parent)
