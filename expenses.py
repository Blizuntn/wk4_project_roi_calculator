class Expenses:
    def __init__(self):
        self.expense_name = {}
        self.name = ""
        self.amount = ""
        self.expense_amount = {}
        self.amount_list = []

    def get_expenses(self):
        print("Please enter expense info")
        self.name = input("Please enter an expense name: ")
        self.amount = input("Please enter an expense amount: ")
        return self.name, self.amount

    def add_expenses(self):
        self.get_expenses()
        self.expense_name["name"] = self.name
        self.expense_amount["amount"] = self.amount
        self.amount_list.append(self.amount)
        print(f"You have added {self.amount} to {self.name}.")
        print()
        more_expenses = input("Would you like to add more expenses: Y/N ").lower()
        if more_expenses == "y":
            self.add_expenses()
        else:
            total_expenses = sum(self.amount_list)
            print(f"Your total expenses are ${total_expenses}.")

        return self.expense_name, self.expense_amount
