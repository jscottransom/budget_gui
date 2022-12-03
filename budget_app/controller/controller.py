import sys
import os

sys.path.append(os.path.abspath("../"))
from views.budget_view import BudgetView


class BudgetViewController:
    def __init__(self):
        self.view = BudgetView()
        self._updateView()

    def _updateView(self):
        
