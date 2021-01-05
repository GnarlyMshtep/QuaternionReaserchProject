# from Vector import Vector
from Quaternion import Quaternion
from math import cos, degrees, sin, radians, sqrt, prod
from MatansFrange import frange

# static class (module in python). used as a structure to carry out rotations in 3D.
"""
To implement:
1. find combined axis angle pair,
2. rotate around multiple axis
3. ...

"""


# this function allows the user to rotate not starting from 0deg
def rotate3DpointFromToAngle(point: list, axis: list, fromAngle: degrees, toAngle: degrees, incrementBy: degrees) -> Quaternion:
    fromAngle /= 2
    toAngle /= 2
    incrementBy /= 2
    print(frange(fromAngle, toAngle, incrementBy))
    for angle in frange(fromAngle, toAngle, incrementBy):
        pointAsQuaternion = Quaternion(
            True, r=0, x=point[0], y=point[1], z=point[2])

        QuaternionToMultBy = Quaternion(
            False, theta=angle, vec=(axis))

        QuaternionToMultByInverse = QuaternionToMultBy.multiplicativeConjugate()
        resultingQuaternion = (QuaternionToMultBy *
                               pointAsQuaternion) * QuaternionToMultByInverse

        print(f"At angle {angle*2} are at: ", resultingQuaternion)


def rotateAboutMultipleAxis(point: list, axisAnglePairs: list, incrementBy: degrees) -> Quaternion:
    """
    Allows the user to rotate a point about multiple axis at diffrent angles at once (not sequencially) to find the result of the overall
    rotation.
    Example Calling: 
        ((1,1,1), (((0,0,1),": 90),((0,0,1),": 90)),       5)
         point       tuple of tuples of axis angle pairs  degrees inc to print
    """
    qs = []
    for axisAnglePair in axisAnglePairs:
        qs.append(Quaternion(
            False, angle=axisAnglePair[1], vec=axisAnglePair[0]))

    # not needed since the next function will make this calculation for us with greater efficiency
    qInverses = [quaternion.multiplicativeConjugate()
                 for quaternion in reversed(qs)]

    qsProd = prod(qs, start=Quaternion(True, r=1, x=0, y=0, z=0))
    qInversesProd = prod(qInverses, start=Quaternion(True, r=1, x=0, y=0, z=0))\

    print(qsProd, qInversesProd)
    print(qsProd.getPolarRepresentation()["theta"])
    rotate3DpointFromToAngle(
        point, qsProd.getPolarRepresentation()["vec"], 0, qsProd.getPolarRepresentation()["theta"], incrementBy)


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
