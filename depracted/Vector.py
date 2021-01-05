
"""
DEPRECATED
"""


from MathematicalObject import MathematicalObject
from math import sqrt

# shuld instansiate mathematical object but I'm cheating


class Vector():
    """
    standard vector, defined to manipulate points and stuff
    """

    def __init__(self, x: float, y: float, z: float) -> None:
        self = [x, y, z]

    def magnitude(self) -> float:
        return sqrt(self[0]**2+self[1]**2+self[2]**2)

    def normalized(self):
        x = self.magnitude()
        return Vector(self[0]/x, self[1]/x, self[2]/x)

    # def dot(self, other):
     #
