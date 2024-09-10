from abc import ABC, abstractmethod

class Abstrata(ABC):
    @abstractmethod
    def soma(self, a, b):
        ...
    
    @abstractmethod
    def subtracao(self, a, b):
        ...
    
    @abstractmethod
    def multiplicacao(self, a, b):
        ...
    
    @abstractmethod
    def divisao(self, a, b):
        ...
    