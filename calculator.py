from income import Income
from expenses import Expenses
from invesetments import Investments
class Calculator:
    def __init__(self):
        self.income = ""
        self.expenses = ""
        self.investments = ""
    def __repr__(self):
        return
    def find_roi(self, income, expenses, investments):
        income = Income()
        print(income.roi_info)
        expenses = Expenses()
        print(expenses.roi_info)
        investments = Investments()
        print(investments.roi_info)




