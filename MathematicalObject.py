from abc import ABCMeta, abstractmethod
"""
This template may not be in immediate use (since our only object as of now is a quaternion).
Yet, I hope to add more mathematical objects to this list sometime in the future. 
"""


class MathematicalObject(metaclass=ABCMeta):
    @abstractmethod
    def __str__(self, MathematicalObject):
        pass

    @abstractmethod
    def __mul__(self, MathematicalObject):
        pass

    @abstractmethod
    def __add__(self, MathematicalObject):
        pass
