class Property:
    def __init__(self):
        self.name = ""
        self.property_name = {}
    def get_property_name(self):
        self.name = input("Please enter a name for this property: ")
        return self.name
    def add_property_name(self):
        self.get_property_name()
        self.property_name["name"] = self.name
        print(f"You have added {self.name} as a property.")
        return self.property_name
property1 = Property()
property1.add_property_name()
print(property1.property_name)