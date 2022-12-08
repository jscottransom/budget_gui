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


class ActualsView(QVBoxLayout):
    """Class to represent Actuals"""

    def __init__(self, parent=None):
        super(ActualsView, self).__init__(parent)
        self._createForm()
        # Construct Widget for Category

    def _createForm(self):
        self.label = QLabel("Unsubmitted")
        self.addRow(self.label)
        self.addRow("Month:", QLineEdit())
        self.addRow("Year:", QLineEdit())
