class User:
    def __init__(self, name):
        self.name = name



class CoffeMachine:

    def __init__(self, code, menu, color=None):
        self.code = code
        self.menu = menu
        self.color = "Red" if color is None else color

    def __repr__(self):
        return f"Its Code: {self.code}, Color:{self.color}"

class Menu:
    def __init__(self,menu_items, num_page, color=None):
        self.menu_items = menu_items
        self.num_page = num_page
        self.color = "white" if color is None else color

    def __repr__(self):
        return f"Menu pages: {self.num_page}, Its color: {self.color}"

class MenuItem:
    def __init__(self, name, cost, size, water, milk, coffe):
        self.name = name
        self.cost = cost
        self.size = size
        self.water = water
        self.milk = milk
        self.coffe = coffe

    def __repr__(self):
        return f"Drink: {self.name}, {self.cost}$, Size: {self.size}"


hamody = User("Hamody")
dodo = User("dodo")

menu_items =[
    MenuItem(name="latte", water=200, milk=150, coffe=24, cost=2.5, size="M"),
    MenuItem(name="espresso", water=50, milk=0, coffe=18, cost=1.5, size="L"),
    MenuItem(name="cappuccino", water=250, milk=50, coffe=24, cost=3, size="S")
]
stenz_menu = Menu(menu_items, 4)
stenz_coffe_machine = CoffeMachine(1751999, stenz_menu, "purple")

print(hamody.name)
print(stenz_menu)
for item in stenz_menu.menu_items:
    print(item)

print(stenz_coffe_machine)