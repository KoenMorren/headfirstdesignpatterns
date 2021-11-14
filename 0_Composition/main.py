import duck
import duck_with_behaviour
import quack_behaviour

print("When just using inheritance, RubberDucks can Quack")
d = duck.Mallard()
d.Display()
d.Quack()

e = duck.RubberDuck()
e.Display()
e.Quack()

print()
print("This problem can be resolved by moving the quack behaviour out of the inheritance chain")
f = duck_with_behaviour.Mallard()
f.Display()
f.Quack()

g = duck_with_behaviour.RubberDuck()
g.Display()
g.Quack()
# The QuackBehaviour can be changed at run time
g.QuackBehaviour = quack_behaviour.Quack() 
g.Quack()