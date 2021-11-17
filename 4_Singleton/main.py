from boiler import Boiler

# throws an error
#a = Boiler()

b = Boiler.instance()
c = Boiler.instance()

print(b)
print(c)