from abc import ABC

class Duck():
    name = "Duck"

    def Display(self):
        print(self.name)

    def Quack(self):
        print(self.name + " let's out a load QUACK.")

    def Swim(self):
        print(self.name + " is swimming.")

class Mallard(Duck):
    def __init__(self):
        super().__init__()
        self.name = "Mallard"

class RubberDuck(Duck):
    def __init__(self):
        super().__init__()
        self.name = "Rubber Duck"
    
    # RubberDuck now can Quack?