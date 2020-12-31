from MathematicalObject import MathematicalObject
from math import sqrt

ERROR = .0005
PRECISION = 4


def sign(x): return "+" if x >= 0 else("-")

# look into redifining everything in term of dictionaries and list (more pythonic)

# Cartesian!!!

"""
      def __init__(self, cartesian: bool, r: float, i: float, j: float, k: float):
        if cartesian:
            self.r = r
            self.i = i
            self.j = j
            self.k = k
        else: 
"""


# let the user define in polar form, no need to worry about updating since quaternions are never updated, I always return a new object.
class Quaternion(MathematicalObject):
    def __init__(self, r: float, i: float, j: float, k: float):
        self.r = r
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        # return str(self.r) + " + "+str(self.i) + "i+ "+str(self.j) + "j+ "+str(self.k)+"k"
        # return f"{round(self.r,3)}+{round(self.i,3)}i+{round(self.j,3)}j+{round(self.k,3)}k"
        return f"{sign(self.r)}{abs(round(self.r, PRECISION))} {sign(self.i)}{abs(round(self.i, PRECISION))}i {sign(self.j)}{ abs(round(self.j, PRECISION))}j { sign(self.k)}{abs(round(self.k, PRECISION))}k "
        # return f"{{round(self.r,3)}+{round(self.i,3)}i+{round(self.j,3)}j+{round(self.k,3)}k"

    def __mul__(self, q2):
        if (isinstance(q2, Quaternion)):
            return Quaternion(self.r*q2.r-self.i*q2.i-self.j*q2.j-self.k*q2.k,
                              self.r*q2.i+self.i*q2.r+self.j*q2.k-self.k*q2.j,
                              self.r*q2.j+self.j*q2.r+self.k*q2.i-self.i*q2.k,
                              self.r*q2.k+self.k*q2.r+self.i*q2.j-self.j*q2.i)
        else:
            return Quaternion(self.r*q2, self.i*q2, self.j*q2, self.k*q2)

    # spent about an hr figuring out that __div__ is no longer supported 🤬🤬
    def __truediv__(self, other):
        if(isinstance(other, Quaternion)):
            return self.__mul__(other.multiplicativeConjugate())
        if(isinstance(other, (float, int))):
            return Quaternion(self.r/other, self.i/other, self.j/other, self.k/other)
        else:
            return NotImplemented

    def __add__(self, q2):
        return Quaternion(self.r+q2.r, self.i+q2.i, self.j+q2.j, self.k+q2.k)

    def __sub__(self, q2):
        return Quaternion(self.r-q2.r, self.i-q2.i, self.j-q2.j, self.k-q2.k)

    def mod(self):
        return sqrt(self.r**2+self.i**2+self.j**2+self.k**2)

    def magnitude(self):
        return self.mod()

    def AdditiveConjugate(self):
        return Quaternion(-self.r, -self.i, -self.j, -self.k)

    def multiplicativeConjugate(self):
        x = self.magnitude()**2
        return Quaternion(self.r/x, -self.i/x, -self.j/x, -self.k/x)

    def isUnitQuaternion(self):
        return (abs(self.magnitude()-1) < ERROR)

    def __pow__(self, power):
        if(isinstance(power, int)):
            x = self
            for i in range(1, power):
                x = x*self
            return x
        else:
            raise NotImplemented

    def pointToQuaternion(point):
        pass

    # logarithm of quaternion? square roots? exponets?
# end of quaternion class
