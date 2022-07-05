class Expenses:
    roi = {}
    def __init__(self):
        self.name = ""
        self.amount = ""
        self.expense_list = []
        self.total = ""
    def __repr__(self):
        return self.name
    def create_expense(self):
        expense = Expenses()
        expense.name = input("Enter the name for this expense: ")
        expense.amount = int(input("Enter the amount for this expense: "))
        expense.additions = input("Would you like to add another expense: Y/N ")
        while expense.additions == "y":
            expense.amount = int(input("Enter the amount for this expense: "))
            expense.additions = input("Would you like to add another expense: Y/N ")
        expense.expense_list.append(expense.amount)
        expense.total = sum(expense.expense_list)
        self.roi[f"{expense.name}"] = expense.total
        return f"You have entered {expense.total} in total for {expense.name}."


