import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFormLayout,
    QRadioButton,
    QLabel,
    QCheckBox,
    QStatusBar,
    QListWidget,
    QWidget,
    QStackedWidget
)
from functools import partial
from views.budget_view import BudgetView
from views.actuals_view import ActualsView

class FinancialsApp(QWidget):
    """
    Stacked structure for Multi Page GUI 
    """
    def __init__(self):

        super(FinancialsApp, self).__init__()
        self.controlPanel = QListWidget ()
        self.controlPanel.insertItem (0, 'Budgeting' )
        self.controlPanel.insertItem (1, 'Income' )
        self.controlPanel.insertItem (2, 'Expenses' )
        
        
        self.budget = QWidget()
        self.income = QWidget()
        self.expenses = QWidget()
        
        self.budgetUI()
        self.incomeUI()
        self.expensesUI()
        
        self.Stack = QStackedWidget (self)
        self.Stack.addWidget (self.budget)
        self.Stack.addWidget (self.income)
        self.Stack.addWidget (self.expenses)
        
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.controlPanel)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)
        self.controlPanel.currentRowChanged.connect(self.display)
        self.setGeometry(300, 50, 10,10)
        self.setWindowTitle('DFY Budgeting & Analysis')
        self.show()
    
    def budgetUI(self):
        budgetlayout = BudgetView()
        self.budget.setLayout(budgetlayout)
            
    def incomeUI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("Male"))
        sex.addWidget(QRadioButton("Female"))
        layout.addRow(QLabel("Sex"),sex)
        layout.addRow("Date of Birth",QLineEdit())
            
        self.income.setLayout(layout)
            
    def expensesUI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("subjects"))
        layout.addWidget(QCheckBox("Physics"))
        layout.addWidget(QCheckBox("Maths"))
        self.expenses.setLayout(layout)
            
    def display(self,i):
        self.Stack.setCurrentIndex(i)
            
def main():
   app = QApplication([])
   ex = FinancialsApp()
   ex.show()
   sys.exit(app.exec())
	
if __name__ == '__main__':
   main()