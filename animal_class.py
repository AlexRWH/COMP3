import random

class Animal:
    """A Generic Reprsentation of a Animal"""

    #Constructor
    def __init__(self,growth_rate,food_need,water_need):
        #set the attributes with an intial value
        self._weight = 1
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._status = "Baby"
        self._type = "Generic"
        self._name = "Generic"
        #the above attributes are prefixed with an underscore to indicate
        #that they should not be accessed directly from outwith the class

    #Methods       
    def needs(self):
        #returns a dictionary containing the food and water needs
        return{'food need':self._food_need, 'water need':self._water_need}

    def report(self):
        #returns a dictionary containing the type, status, weight ,days growing
        return{'type':self._type, 'status':self._status ,'weight':self._weight ,'days growing':self._days_growing}

    def update_status(self):
        if self._weight > 50:
            self._status = "Mature"
        elif self._weight > 35:
            self._status = "Adult"
        elif self._weight > 15:
            self._status = "Young Adult"
        elif self._weight > 1:
            self._status = "Young"
        elif self._weight == 1:
            self._status = "Baby"

    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            self._weight += self._growth_rate
        #incremeant days growing
        self._days_growing += 1
        #update staus
        self.update_status()

def auto_grow(animal,days):
    for day in range(days):
        food = random.randint(1,10)
        water = random.randint(1,10)
        animal.grow(food, water)

def manual_grow(animal):
 #get the food and water values from the user
    valid = False
    while not valid:
        try:
            food = int(input("Please enter a food value (1-10):"))
            if 1 <= food <= 10:
                valid = True
            else:
                print("Value entered not valid - Please enter a value between 1-10")
        except ValueError:
            print("Value entered not valid - Please enter a value between 1-10")
    valid = False
    while not valid:
        try:
            water = int(input("Please enter a water value (1-10):"))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Value entered not valid - Please enter a value between 1-10")
        except ValueError:
            print("Value entered not valid - Please enter a value between 1-10")

    
def display_menu():
    print("1. Grow manualy over 1 day")
    print("2. Grow automatically for 30 days ")
    print("3. Report Status")
    print("0. Exit test Program")
    print()
    print("please select an option from the above menu")

def get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option Selected: "))
            if 0 <= choice <= 4:
                    option_valid = True
            else:
                print("Please enter a valid option")
        except:
            print("Please enter a valid option")
    return choice

def manage_animal(animal):
    print("This is the farm animal Management Program")
    print()
    noexit = True
    while noexit:
        display_menu()
        option = get_menu_choice()
        print()
        if option == 1:
            manual_grow(animal)
            print()
        elif option == 2:
            auto_grow(animal,30)
            print()
        elif option == 3:
            print(animal.report())
            print()
        elif option == 0:
            noexit = False
            print()
    print("Thank you for using the farm animal management program")

def main():
    #instantiate the class
    new_animal = Animal(1,5,7)
    manage_animal(new_animal)
    
if __name__ == "__main__":
    main()
