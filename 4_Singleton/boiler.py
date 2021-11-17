class Boiler:
    _empty = True
    _boiled = False

    _instance = None

    def __init__(self):
        raise RuntimeError('Cannot instantiate the singleton class. Use .instance() instead.')

    @classmethod
    def instance(self):
        if self._instance is None:
            print("Creating a new instance of the Boiler")
            self._instance = self.__new__(Boiler)
        
        return self._instance

    def fill(self):
        self._empty = False
        print('Filled the boiler with milk')
    
    def boil(self):
        self._boiled = True
        print('Boiled the contents of the boiler')

    def empty(self):
        self._empty = True
        self._boiled = False
        print('Emptied the contents of the boiler into the vat')