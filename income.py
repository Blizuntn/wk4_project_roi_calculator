class Income:
    def __init__(self):
        self.name = ""
        self.income_name = {}
        self.amount = ""
        self.income_amount = {}
        self.amount_list = []

    def get_income(self):
        print("Please enter income information")
        self.name = input("What is the income name: ")
        self.amount = int(input("What is the amount of income: "))
        return self.name, self.amount

    def add_income(self):
        self.get_income()
        self.income_name["name"] = self.name
        self.income_amount["amount"] = self.amount
        self.amount_list.append(self.amount)
        print(f"You have added {self.amount} to {self.name}.")
        print()
        more_income = input("Would you like to add more income: Y/N ").lower()
        if more_income == "y":
            self.add_income()
        else:
            total_income = sum(self.amount_list)
            print(f"You have total income of ${total_income}.")

        return self.income_name, self.income_amount
income1 = Income()
income1.add_income()