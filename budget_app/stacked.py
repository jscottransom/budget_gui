import sys
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QListWidget,
    QWidget,
    QStackedWidget,
)

from views.budget_view import BudgetView
from views.income_view import IncomeView
from views.expenses_view import ExpensesView


class FinancialsApp(QWidget):
    """
    Stacked structure for Multi Page GUI
    """

    def __init__(self):
        """
        Constructor for the FinancialsApp Class, which inherits the generic QWidget properties.
        """

        super(FinancialsApp, self).__init__()

        # Instantiate Side Panel With Options
        self.controlPanel = QListWidget()
        self.controlPanel.insertItem(0, "Budgeting")
        self.controlPanel.insertItem(1, "Income")
        self.controlPanel.insertItem(2, "Expenses")

        # Build Widget
        self.budget = QWidget()
        self.income = QWidget()
        self.expenses = QWidget()

        # Call the methods which create the individual Budget, Income and Expenses Pages
        self.budgetUI()
        self.incomeUI()
        self.expensesUI()

        # Add the pages to the QStackedWidget object.
        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.budget)
        self.Stack.addWidget(self.income)
        self.Stack.addWidget(self.expenses)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.controlPanel)
        hbox.addWidget(self.Stack)

        # Window Specs
        self.setLayout(hbox)
        self.controlPanel.currentRowChanged.connect(self.display)
        self.setGeometry(300, 50, 10, 10)
        self.setWindowTitle("DFY Budgeting & Analysis")
        self.show()

    def budgetUI(self):
        """
        Display the BudgetView for submission to the BigQuery Columnar Database.
        """
        budgetlayout = BudgetView()
        self.budget.setLayout(budgetlayout)

    def incomeUI(self):
        """
        Display the Income View for an accurate representation of income.
        """
        incomeLayout = IncomeView()
        self.income.setLayout(incomeLayout)

    def expensesUI(self):
        """
        Display the Expenses View for an accurate representation of income.
        """
        expensesLayout = ExpensesView()
        self.expenses.setLayout(expensesLayout)

    def display(self, i):
        """
        Set the current index of the side panel to determine which page to display.
        """
        self.Stack.setCurrentIndex(i)


def main():
    # Instantiate app, display window and exit.
    app = QApplication([])
    ex = FinancialsApp()
    ex.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
