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
    QStatusBar,
    QWidget,
)
from functools import partial
from views.budget_view import BudgetView

WINDOW_SIZE = 235
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40
ERROR_MSG = "ERROR"


class BudgetAppWindow(QMainWindow):

    """DFY Budget App main window (GUI or view)."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("DFY Budgeting & Analysis")
        # centralWidget = QWidget(self)
        # self.setCentralWidget(centralWidget)
        self._createStatusBar()
        self.initUI()

    def initUI(self):
        centralWidget = QWidget()
        self.budgetlayout = BudgetView(centralWidget)
        self.setCentralWidget(centralWidget)
        
        

    def _createStatusBar(self):

        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)

    # def _createBudgetView(self):
    #     "test"
    #     # self.budget = BudgetView()
    #     # self.budgetview.show()


def main():

    """Budget App main function."""
    BudgetApp = QApplication([])
    budgetappWindow = BudgetAppWindow()
    budgetappWindow.show()
    sys.exit(BudgetApp.exec())


if __name__ == "__main__":
    main()
