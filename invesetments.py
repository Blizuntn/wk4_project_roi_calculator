class Investments:
    roi = {}
    def __init__(self):
        self.name = ""
        self.amount = ""
        self.investment_list = []
        self.total = ""
        self.additions = ""
    def __repr__(self):
        return self.name

    def create_investment(self):
        investment = Investments()
        investment.name = input("Enter a name for this investment: ")
        investment.amount = int(input("Enter an amount for this investment: "))
        investment.additions = input("Would you like to add an additional investment: Y/N ")
        while investment.additions == "y":
            investment.amount = int(input("Enter an amount for this investment: "))
            investment.additions = input("Would you like to add an additional investment: Y/N ")
        investment.investment_list.append(investment.amount)
        investment.total = sum(investment.investment_list)
        self.roi[f"{investment.name}"] = investment.total
        return f"You have entered {investment.total} in total for {investment.name}."

