from income import Income
from expenses import Expenses
from invesetments import Investments

class Property:
    def __init__(self):
        self.name = ""
        self.property_list = []
        self.property_name = {}
        self.modify = ""

    def __repr__(self):
        return self.name


    def create_property(self):
        propertie = Property()
        propertie.name = input("Enter the name for this property: ").title()
        propertie.property_name["name"] = f"{propertie.name}"
        return propertie.name

    def choose_property(self):
        propertie = Property()
        propertie.name = input("Which property would you like to see? ")
        return propertie.name

    def modify_property(self):
        propertie = Property()
        propertie.modify = input("Which part of your property do you want to modify? Income/Expenses/Investments: ")\
            .lower()
        if propertie.modify == "income":
            income = Income()
            income.create_income()
        elif propertie.modify == "expenses":
            expenses = Expenses()
            expenses.create_expense()
        elif propertie.modify == "investments":
            investments = Investments()
            investments.create_investment()






    def delete_property(self):
        pass

