from abc import ABC
from quack_behaviour import Quack, Squeak

class Duck(ABC):
    _name = "Duck"
    _quackBehaviour = Quack()

    def Display(self):
        print(self._name)

    def Quack(self):
        self._quackBehaviour.Quack()

    @property
    def QuackBehaviour(self):
        return self._quackBehaviour

    @QuackBehaviour.setter
    def QuackBehaviour(self, value):
        self._quackBehaviour = value

class Mallard(Duck):
    def __init__(self):
        super().__init__()
        self._name = "Mallard"
        # self.quackBehaviour = Quack()

class RubberDuck(Duck):
    def __init__(self):
        super().__init__()
        self._name = "Rubber Duck"
        self.QuackBehaviour = Squeak()