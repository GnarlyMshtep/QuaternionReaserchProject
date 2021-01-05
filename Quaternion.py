from MathematicalObject import MathematicalObject
from math import sqrt, cos, sin, radians, acos, degrees

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
    def __init__(self, isCartesian: bool,  **kwargs):
        """
            2 quaternion forms and 2 possible intialization specified by the first bool parameter:
                Cartesian: H = r + xi + yj + zk. Specify r=, x=, y=, and z=. 
                Polar = H = ||H||(e^(n̂θ)) = ||H||(cosθ + sinθ(x, y, z)) specify theta=degress, and vec= 3-list. note that the vector doesn't have to be normlized, 
                we'll do that for you!
            EXAMPLE:
                A = Quaternion(True, r=0.42, x=.68, y=.33, z=.5)
                B = Quaternion(False, theta=65, vec=[.75, .36, .55])
        """
        if isCartesian:
            self.r = kwargs["r"]
            self.i = kwargs["x"]
            self.j = kwargs["y"]
            self.k = kwargs["z"]

        else:
            magnitude = sqrt(sum([i**2 for i in kwargs["vec"]]))

            #normalizedVec = [j / magnitude for j in kwargs["vec"]]
            # now that we normalized our vector we can set up the cartesian properties that we plan to use

            # used so we don't reapet this part of the calculation

            if "angle" in kwargs.keys():
                kwargs["theta"] = kwargs["angle"]

            temp = sin(radians(kwargs["theta"]))

            self.r = magnitude * cos(radians(kwargs["theta"]))
            self.i = kwargs["vec"][0] * temp
            self.j = kwargs["vec"][1] * temp
            self.k = kwargs["vec"][2] * temp

    def __str__(self):
        # return str(self.r) + " + "+str(self.i) + "i+ "+str(self.j) + "j+ "+str(self.k)+"k"
        # return f"{round(self.r,3)}+{round(self.i,3)}i+{round(self.j,3)}j+{round(self.k,3)}k"
        return f"{sign(self.r)}{abs(round(self.r, PRECISION))} {sign(self.i)}{abs(round(self.i, PRECISION))}i {sign(self.j)}{ abs(round(self.j, PRECISION))}j { sign(self.k)}{abs(round(self.k, PRECISION))}k "
        # return f"{{round(self.r,3)}+{round(self.i,3)}i+{round(self.j,3)}j+{round(self.k,3)}k"

    def __repr__(self):
        return f"{sign(self.r)}{abs(round(self.r, PRECISION))} {sign(self.i)}{abs(round(self.i, PRECISION))}i {sign(self.j)}{ abs(round(self.j, PRECISION))}j { sign(self.k)}{abs(round(self.k, PRECISION))}k "

    def __mul__(self, q2):
        if (isinstance(q2, Quaternion)):
            return Quaternion(True, r=self.r*q2.r-self.i*q2.i-self.j*q2.j-self.k*q2.k,
                              x=self.r*q2.i+self.i*q2.r+self.j*q2.k-self.k*q2.j,
                              y=self.r*q2.j+self.j*q2.r+self.k*q2.i-self.i*q2.k,
                              z=self.r*q2.k+self.k*q2.r+self.i*q2.j-self.j*q2.i)
        else:
            return Quaternion(True, r=self.r*q2, x=self.i*q2, y=self.j*q2, z=self.k*q2)

    # spent about an hr figuring out that __div__ is no longer supported 🤬🤬
    def __truediv__(self, other):
        if(isinstance(other, Quaternion)):
            return self.__mul__(other.multiplicativeConjugate())
        if(isinstance(other, (float, int))):
            return Quaternion(True, r=self.r/other, x=self.i/other, y=self.j/other, z=self.k/other)
        else:
            return NotImplemented

    def __add__(self, q2):
        return Quaternion(True, r=self.r+q2.r, x=self.i+q2.i, y=self.j+q2.j, z=self.k+q2.k)

    def __sub__(self, q2):
        return Quaternion(True, r=self.r-q2.r, x=self.i-q2.i, y=self.j-q2.j, z=self.k-q2.k)

    def mod(self):
        return sqrt(self.r**2+self.i**2+self.j**2+self.k**2)

    def magnitude(self):
        return self.mod()

    def AdditiveConjugate(self):
        return Quaternion(True, r=-self.r, x=-self.i, y=-self.j, z=-self.k)

    def multiplicativeConjugate(self):
        m = self.magnitude()**2
        return Quaternion(True, r=self.r/m, x=-self.i/m, y=-self.j/m, z=-self.k/m)

    def isUnitQuaternion(self):
        return (abs(self.magnitude()-1) < ERROR)

    def getPolarRepresentation(self) -> dict:
        """
        returns a dictionary such that
        (magnitude) *(cos(theta)+ sin(theta)(vec)) 
        and magnitude, theta, and vec are the accessible values
        """
        mag = self.magnitude()
        normalized = self/mag
        theta = acos(normalized.r)

        # guard from div by 0 when we don't rotate at all
        divisor = 1 if sin(theta) == 0 else sin(theta)

        return {
            "magnitude": mag,
            "theta": degrees(theta),
            "angle": degrees(theta),
            "vec": (self.i/divisor, self.j/divisor, self.k/divisor),
        }

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
