from observer import IObserver

class DisplayElement(IObserver):
    _name = ''

    def __init__(self, name):
        self._name = name

    def update(self, newValue):
        print(self._name + " has received a new value of : " + str(newValue))