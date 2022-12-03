import sys
import logging

from PyQt6 import QtGui, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QFormLayout,
    QPushButton,
    QLineEdit,
    QComboBox,
    QLabel,
    QWidget,
    QFileDialog,
)
from functools import partial


class BudgetView(QFormLayout):
    """Class to represent budget form input"""

    def __init__(self, parent=None):
        super(BudgetView, self).__init__(parent)
        self._createForm()
        # Construct Widget for Category

    def updateCategory(self, index):
        # first of all, clear the current contents of the combo
        self.categoryBox.clear()
        # then, add the new items, based on the new index
        categories = self.TypeBox.itemData(index)

        # Construct Widget for Category
        forecast_sub_cat = ["Fees", "Contracted Group", "FITs", "Cruising", "Ancillary"]
        direct_sub_cat = ["Fees"]
        commission_sub_cat = ["Contracted Group", "FITs", "Cruising", "Ancillary"]
        expenses_sub_cat = [
            "Accounting/Insurance",
            "Membership/License",
            "Marketing Funnel",
            "Travel/Training",
            "Client Docs / Gifts",
            "Communication",
            "Website",
            "Office",
            "Subscription",
        ]
        category_sublists = [
            forecast_sub_cat,
            direct_sub_cat,
            commission_sub_cat,
            expenses_sub_cat,
        ]

        self.categoryBox.addItems(category_sublists[index])

    def updateGrouping(self, index):
        # first of all, clear the current contents of the combo
        self.groupingBox.clear()
        # then, add the new items, based on the new index

        # Collect Type Box information
        TypeBox = self.TypeBox.currentText()

        if TypeBox == "Forecast":
            forecast_groupings = {
                "Fees": ["Individual", "Small Group", "Large Group"],
                "Contracted Group": [
                    "GoWay",
                    "GoGo Vacations",
                    "Classic Vacations",
                    "Globus",
                    "Other",
                ],
                "Cruising": ["Ocean", "River"],
                "FITs": [
                    "Delta Vacations",
                    "American Airlines Vacations",
                    "GoGo Vacations",
                    "Other",
                ],
                "Ancillary": ["Project Expedition", "Travel Insurance", "Other"],
            }

        elif TypeBox == "Direct":
            forecast_groupings = {
                "Fees": ["Individual", "Small Group", "Large Group"],
            }
        elif TypeBox == "Commission":
            forecast_groupings = {
                "Contracted Group": [
                    "GoWay",
                    "GoGo Vacations",
                    "Classic Vacations",
                    "Globus",
                    "Other",
                ],
                "Cruising": ["Ocean", "River"],
                "FITs": [
                    "Delta Vacations",
                    "American Airlines Vacations",
                    "GoGo Vacations",
                    "Other",
                ],
                "Ancillary": ["Project Expedition", "Travel Insurance", "Other"],
            }

        else:
            forecast_groupings = {
                "Accounting/Insurance": ["Travel Joy", "Berkshire Hathaway"],
                "Memberhsip/License": [
                    "ASTA",
                    "Travel Institute",
                    "Hosting",
                    "TMM",
                    "Other",
                ],
                "Marketing Funnel": [
                    "Email Marketing Platform",
                    "Design Software",
                    "Quiz Builder",
                    "Social Media Manager",
                    "Ads Campaign",
                    "Weekly Content Creation",
                    "Other",
                ],
                "Travel/Training": [
                    "Phone",
                    "Mi-fi",
                    "Internet",
                    "Misc",
                    "Registration",
                    "Air",
                    "Lodging",
                    "Meals",
                    "Other",
                ],
                "Client Docs / Gifts": ["Amazon", "Postage", "Boxes", "Other"],
                "Communication": ["Phone", "Internet", "Mi-fi", "Other"],
                "Website": ["Domain", "Wix", "Email", "Other"],
                "Office": ["Other"],
                "Subscription": ["Other"],
            }

        if self.categoryBox.currentText() != '':
            self.groupingBox.addItems(
            forecast_groupings[self.categoryBox.currentText()]
        )

    def pressed_submit(self):
        """
        When the user presses the submit button, the form is submitted.
        """
        # Get the values from the form
        # Collect all inputs
        # Upload to database
        # Clear Form
        self.label.setText("You've pressed submit")
        self.amountobj.clear()

    def bulk_upload(self):
        """
        When the user presses the submit button, the form is submitted.
        """
        # Get the values from the form
        self.label.setText("You've pressed submit")

    def open (self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
        print(f"Path to file : {filename}")

    def browse_data1(self):
        data_path=QFileDialog.getOpenFileName(None,'Open File',"/Users/jscoran/GUI",'*',)
        # Open File and upload to database
        # with open('data_path', 'r') as handle:
        #     _pickle.dump(data_path,handle,protocol=_pickle.HIGHEST_PROTOCOL)


    def _createForm(self):
        self.label = QLabel("Unsubmitted")
        self.addRow(self.label)
        self.addRow("Month:", QLineEdit())
        self.addRow("Year:", QLineEdit())

        # Construct Widget for Type
        self.TypeBox = QComboBox()
        self.TypeBox.addItems(["Forecast", "Direct", "Commission", "Expense"])
        self.addRow("Type", self.TypeBox)

        self.categoryBox = QComboBox()
        self.addRow("Category", self.categoryBox)

        self.groupingBox = QComboBox()
        self.addRow("Grouping", self.groupingBox)

        self.TypeBox.currentIndexChanged.connect(self.updateCategory)
        self.updateCategory(self.TypeBox.currentIndex())

        self.categoryBox.currentIndexChanged.connect(self.updateGrouping)
        self.updateGrouping(self.categoryBox.currentIndex())

        self.addRow("Comment:", QLineEdit())
        self.addRow("Quantity", QLineEdit())
        self.addRow("Commission Paid", QLineEdit())
        self.addRow("Commission Split", QLineEdit())

        self.amountobj = QLineEdit()
        self.addRow("Amount", self.amountobj)

        self.uploadButton = QPushButton("Bulk Upload")
        self.addRow(self.uploadButton)
        self.uploadButton.clicked.connect(self.browse_data1)

        self.addRow(QPushButton("Submit", clicked= lambda: self.pressed_submit()))



    def _createType(self):

        self.setWidget(0, QFormLayout.ItemRole.FieldRole, self.TypeBox)


if __name__ == "__main__":
    BudgetApp = QApplication([])
    window = QWidget()
    budget_view = BudgetView()
    window.setLayout(budget_view)
    window.show()
    sys.exit(BudgetApp.exec())
