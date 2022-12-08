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


class ExpensesView(QVBoxLayout):
    """Expenses"""

    def __init__(self, parent=None):
        super(ExpensesView, self).__init__(parent)
