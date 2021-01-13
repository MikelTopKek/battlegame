from abc import ABC, abstractmethod


class BaseUnit(ABC):
    status = None # TODO:::replace with enum value or other variable
    index: int

    def __init__(self, index: int):
        self.index = index

    def __repr__(self):
        return self.__str__()

    @abstractmethod
    def attack(self, *args, **kwargs):
        pass

