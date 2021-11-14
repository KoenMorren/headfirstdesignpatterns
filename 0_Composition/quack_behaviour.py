from abc import ABC, abstractmethod

class QuackBehaviour(ABC): 
    @abstractmethod
    def Quack(self):
        pass

class Quack(QuackBehaviour):
    def Quack(self):
        print("Quack")

class Squeak(QuackBehaviour):
    def Quack(self):
        print("Squeak")