#from Vector import Vector
from Quaternion import Quaternion
from math import cos, degrees, sin, radians, sqrt

# static class. used as a structure to carry out rotations in 3D.
# a point is a list [x,y,z]


# rn no support for interpolation
def rotate3Dpoint(point: list, axis: list, fromAngle: degrees, toAngle: degrees):
    fromAngle /= 2
    toAngle /= 2
    for angle in (fromAngle, toAngle):
        print("In loop")
        pointAsQuaternion = pointToQuaternion(point)
        QuaternionToMultBy = findRotationQuaternion(axis, angle)
        QuaternionToMultByInverse = QuaternionToMultBy.multiplicativeConjugate()
        print("we are at: ", (QuaternionToMultBy * pointAsQuaternion)
              * QuaternionToMultByInverse)


def pointToQuaternion(point: list):
    # Vector(point).normalized()
    return Quaternion(0, point[0], point[1], point[2])


def findRotationQuaternion(axis: list, angle: float):
    normalAxis = normalized(axis)
    return Quaternion(0, sin(radians(angle))*normalAxis[0], sin(radians(angle))*normalAxis[1], sin(radians(angle))*normalAxis[2])

# gets a vectors magnitude


def magnitude(vec: list) -> float:
    return sqrt(vec[0]**2+vec[1]**2+vec[2]**2)

# normalizes a vector


def normalized(vec: list) -> list:
    x = magnitude(vec)
    return [vec[0]/x, vec[1]/x, vec[2]/x]
