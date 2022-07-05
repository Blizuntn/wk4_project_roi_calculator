from properties import Property
from income import Income
from expenses import Expenses
from invesetments import Investments
from user import User
from calculator import Calculator

money = {}
data =[]

def start():
    print(greeting)
    print("Please enter user information")
    user = User().create_user()
    print(f"Congratulations {user} you are the first user")
    print("Please enter property information")
    propertie = Property().create_property()


    print("Please enter income information:")
    print(Income().create_income())
    for key, value in Income().roi.items():
        data.append(value)

    print("Please enter expense information:")
    print(Expenses().create_expense())
    for key, value in Expenses().roi.items():
        data.append(value)

    print("Please enter investment information:")
    print(Investments().create_investment())
    for key, value in Investments.roi.items():
        data.append(value)

    roi = round(((((data[0] - data[1]) * 12) / data[2]) * 100),2)
    money[f"{propertie}"] = f"{roi}%"

    print(f"The Cash on Cash ROI for {propertie} is {roi}%")


greeting = "Welcome to the Best ROI Calculator"
menu = """
[1] Create Property - create a new property and see its ROI
[2] Portfolio
[3] Choose Property - Switch current property
[4] Modify Property
[5] Delete Property
[6] Create User
[7] Switch Users
[0] Quit
"""


def calculator():
    start()
    is_on = True
    while is_on:
        print(menu)
        data.clear()
        get_input = input("What would you like to do? Please enter a number: ")
        if get_input == "1":
            propertie = Property().create_property()
            print("Please enter income information")
            print(Income().create_income())
            for key, value in Income().roi.items():
                data.append(value)

            print("Please enter expense information:")
            print(Expenses().create_expense())
            for key, value in Expenses().roi.items():
                data.append(value)

            print("Please enter investment information:")
            print(Investments().create_investment())
            for key, value in Investments.roi.items():
                data.append(value)

            roi = round(((((data[0] - data[1]) * 12) / data[2]) * 100), 2)
            money[f"{propertie}"] = f"{roi}%"
            print(f"The Cash on Cash ROI for {propertie} is {roi}%")
        elif get_input == "2":
            pass
        elif get_input == "3":
            Property().choose_property()
        elif get_input == "4":
            Property().modify_property()
        elif get_input == "5":
            pass
        elif get_input == "6":
            data.clear()
            print("Please enter user information")
            user = User().create_user()
            print(f"{user} has been added as a user.")
            print("Please enter property information")
            propertie = Property().create_property()

            print("Please enter income information:")
            print(Income().create_income())
            for key, value in Income().roi.items():
                data.append(value)

            print("Please enter expense information:")
            print(Expenses().create_expense())
            for key, value in Expenses().roi.items():
                data.append(value)

            print("Please enter investment information:")
            print(Investments().create_investment())
            for key, value in Investments.roi.items():
                data.append(value)

            roi = round(((((data[0] - data[1]) * 12) / data[2]) * 100), 2)
            money[f"{propertie}"] = f"{roi}%"

            print(f"The Cash on Cash ROI for {propertie} is {roi}%")
        elif get_input == "7":
            pass
        elif get_input == "0":
            is_on = False







calculator()


User()
Property()
Income()
Expenses()
Investments()