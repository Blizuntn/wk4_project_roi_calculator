class Investments:
    def __init__(self):
        self.name = ""
        self.investment_name = {}
        self.amount = ""
        self.investment_amount = {}
        self.amount_list = []

    def get_investment(self):
        print("Please enter investment information")
        self.name = input("What is the investment name: ")
        self.amount = int(input("What is the amount of the investment: "))
        return self.name, self.amount

    def add_investment(self):
        self.get_investment()
        self.investment_name["name"] = self.name
        self.investment_amount["amount"] = self.amount
        self.amount_list.append(self.amount)
        print(f"You have added {self.amount} to {self.name}.")
        print()
        more_investment = input("Would you like to add another investment: Y/N ").lower()
        if more_investment == "y":
            self.add_investment()
        else:
            total_investment = sum(self.amount_list)
            print(f"You have total investment of ${total_investment}.")

        return self.investment_name, self.investment_amount