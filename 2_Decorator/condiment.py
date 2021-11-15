from abc import abstractmethod
from beverage import IBeverage

class ICondimentDecorator(IBeverage):

    _beverage : IBeverage
    _cost = 0
    _description = ''

    @abstractmethod
    def getDescription(self):
        return self._beverage.getDescription() + ', ' + self._description

    @abstractmethod
    def getCost(self):
        return self._beverage.getCost() + self._cost

####

class Milk(ICondimentDecorator):

    def __init__(self, beverage : IBeverage):
        self._beverage = beverage
        self._cost = 1
        self._description = 'Milk'

    def getDescription(self):
        return super().getDescription()

    def getCost(self):
        return super().getCost()

class Mocha(ICondimentDecorator):

    def __init__(self, beverage : IBeverage):
        self._beverage = beverage
        self._cost = 2
        self._description = 'Mocha'

    def getDescription(self):
        return super().getDescription()

    def getCost(self):
        return super().getCost()