import Quaternion as qt
from math import cos, degrees, sin, radians


class PolarQuaternion(qt.Quaternion):
    """
    a daughter to quaternion, extends the same funcitonality but initialized as polar, 
    the form: cos(θ) + sin(θ)(x, y, z) 
    """

    def __init__(self, theta: degrees, x: float, y: float, z: float):
        """ Theta is assumed to be in degrees"""
        super().__init__(cos(radians(theta)), sin(radians(theta))
                         * x, sin(radians(theta))*y, sin(radians(theta))*z)
