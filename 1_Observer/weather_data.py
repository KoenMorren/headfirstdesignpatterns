from subject import ISubject
from observer import IObserver

class WeatherData(ISubject):
    _observers = []
    _value = 0

    def updateValue(self):
        self._value += 1
        self.notifyObservers()

    def registerObserver(self, observer : IObserver):
        self._observers.append(observer)

    def removeObserver(self, observer : IObserver):
        self._observers.remove(observer)

    def notifyObservers(self):
        for observer in self._observers:
            observer.update(self._value)

        print()