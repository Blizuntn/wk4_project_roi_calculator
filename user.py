class User:
    def __init__(self):
        self.user_name = {}
        self.name = ""

    def get_name(self):
        self.name = input("Enter a user name: ")
        return self.name

    def add_user(self):
        self.get_name()
        print(f"{self.name} has been added as a user")
        self.user_name["name"] = self.name
        return self.user_name

user1 = User()
user1.add_user()
