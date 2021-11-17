from abc import ABC, abstractmethod
import pizza_newyork
import pizza_chicago

class PizzaStore(ABC):
    def orderPizza(self, name):
        pizza = self.createPizza(name)

        pizza.bake()
        pizza.cut()
        pizza.box()

    @abstractmethod
    def createPizza(self, name):
        pass

###

class NewYorkPizzaStore(PizzaStore):
    def orderPizza(self, name):
        return super().orderPizza(name)

    def createPizza(self, name):
        switcher= {
            "Cheese": pizza_newyork.CheesePizza(),
            "Peperoni": pizza_newyork.PeperoniPizza()
        }
        return switcher.get(name, "invalid pizza")

class ChicagoPizzaStore(PizzaStore):
    def orderPizza(self, name):
        return super().orderPizza(name)

    def createPizza(self, name):
        switcher= {
            "Cheese": pizza_chicago.CheesePizza(),
            "Peperoni": pizza_chicago.PeperoniPizza()
        }
        return switcher.get(name, "invalid pizza")