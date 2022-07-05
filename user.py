from properties import Property
from income import Income
from expenses import Expenses
from invesetments import Investments


class User:
    def __init__(self):
        self.name = ""
        self.user_name = {}
        self.user_list = []
        self.property_ = Property()
        self.income = Income()
        self.expenses = Expenses()
        self.investments = Investments()

    def __repr__(self):
        return self.name

    def create_user(self):
        user = User()
        user.name = input("Enter a name for this user: ")
        return user.name

    def show_portfolio(self):
        user = User()
        return
