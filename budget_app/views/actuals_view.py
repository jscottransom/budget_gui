import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QFormLayout,
    QLabel,
    QStatusBar,
    QWidget,
)
from functools import partial
from views.budget_view import BudgetView

WINDOW_SIZE = 235
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40
ERROR_MSG = "ERROR"


class ActualsView(QFormLayout):
    """Class to represent budget form input"""

    def __init__(self, parent=None):
        super(BudgetView, self).__init__(parent)
        self._createForm()
        # Construct Widget for Category

    def _createForm(self):
        self.label = QLabel("Unsubmitted")
        self.addRow(self.label)
        self.addRow("Month:", QLineEdit())
        self.addRow("Year:", QLineEdit())