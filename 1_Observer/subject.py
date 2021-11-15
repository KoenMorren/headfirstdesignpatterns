from abc import ABC, abstractmethod
from  observer import IObserver

class ISubject(ABC):
    _observers = []

    @abstractmethod
    def registerObserver(self, observer : IObserver):
        pass

    @abstractmethod
    def removeObserver(self, observer : IObserver):
        pass

    @abstractmethod
    def notifyObservers(self):
        pass