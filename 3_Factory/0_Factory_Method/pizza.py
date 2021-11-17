from abc import ABC

class Pizza(ABC):
    def bake(self):
        print("Bake for 25 mins at 350 degrees")

    def cut(self):
        print("Cutting the pizza in diagonal slices")

    def box(self):
        print("Place the pizza in an official PizzaStore box")