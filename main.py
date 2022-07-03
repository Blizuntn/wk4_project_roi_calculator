from property import Property
from income import Income
from expenses import Expenses
from invesetments import Investments
from user import User
from calculator import Calculator


class Home:
    def __init__(self):
        pass
    def welcome_new_user(self):
        print("Welcome to the Best ROI Calculator")
        get_info = input("Enter a user name: ")

    def get_input(self):
        options = input("""
        What would you like to do? 
        [1] Create Property - create a new property and see its ROI
        [2] Portfolio
        [3] Choose Property - Switch current property
        [4] Modify Property
        [5] Delete Property
        [6] Create User
        [7] Switch Users
        [0] Quit
        
        """)
    def show_main_page(self):
       self.get_input()
main = Home()
main.show_main_page()