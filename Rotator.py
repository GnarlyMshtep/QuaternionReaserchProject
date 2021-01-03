#from Vector import Vector
from Quaternion import Quaternion
from math import cos, degrees, sin, radians, sqrt, trunc
from MatansFrange import frange

# static class. used as a structure to carry out rotations in 3D.
# a point is a list [x,y,z]


# rn no support for interpolation
def rotate3Dpoint(point: list, axis: list, fromAngle: degrees, toAngle: degrees, incrementBy: degrees):
    fromAngle /= 2
    toAngle /= 2
    incrementBy /= 2
    print(frange(fromAngle, toAngle, incrementBy))
    for angle in frange(fromAngle, toAngle, incrementBy):
        pointAsQuaternion = Quaternion(
            True, r=0, x=point[0], y=point[1], z=point[2])

        QuaternionToMultBy = Quaternion(
            False, theta=angle, vec=normalized(axis))

        QuaternionToMultByInverse = QuaternionToMultBy.multiplicativeConjugate()

        print(f"At angle {angle*2} are at: ", (QuaternionToMultBy * pointAsQuaternion)
              * QuaternionToMultByInverse)


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
