import beverage
import condiment

espresso = beverage.Espresso()
print(espresso.getDescription(), espresso.getCost())

espressoWithMilk = condiment.Milk(beverage.Espresso())
print(espressoWithMilk.getDescription(), espressoWithMilk.getCost())

decafWithMilkAndDoubleMocha = condiment.Mocha(condiment.Mocha(condiment.Milk(beverage.Decaf())))
print(decafWithMilkAndDoubleMocha.getDescription(), decafWithMilkAndDoubleMocha.getCost())