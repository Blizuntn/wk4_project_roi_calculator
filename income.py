class Income:
    roi = {}
    def __init__(self):
        self.name = ""
        self.amount = ""
        self.additions = ""
        self.income_list = []
        self.total = ""
    def __repr__(self):
        return self.name
    def create_income(self):
        income = Income()
        income.name = input("Enter the name for this income: ")
        income.amount = int(input("Enter the amount for this income: "))
        income.additions = input("Would you like to add additional income? Y/N ")
        while income.additions == "y":
            income.amount = int(input("Enter amount for this income: "))
            income.income_list.append(income.amount)
            income.additions = input("Would you like to add additional income? Y/N ")
        income.income_list.append(income.amount)
        income.total = sum(income.income_list)
        self.roi[f"{income.name}"] = income.total
        return f"You have entered ${income.total} in total for {income.name}."


