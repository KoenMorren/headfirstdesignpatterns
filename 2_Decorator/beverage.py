from abc import ABC, abstractmethod

class IBeverage(ABC):

    @abstractmethod
    def getDescription(self):
        pass

    @abstractmethod
    def getCost(self):
        pass

####

class Espresso(IBeverage):

    def getDescription(self):
        return "Espresso"

    def getCost(self):
        return 3

class Decaf(IBeverage):

    def getDescription(self):
        return "Decaf"

    def getCost(self):
        return 2