from Quaternion import Quaternion
import Rotator as Rotator
from Encryptor import Encryptor

#print(frange(90, 180, .333))

A = Quaternion(True, r=0.42, x=.68, y=.33, z=.5)
B = Quaternion(False, theta=65, vec=[.75, .36, .55])

#print(A, B)

# esultingPosition = Rotator.rotate3DpointFromToAngle(
#    (1, 0, 0), (1, 1, 1), 0, 75, 1)

x = Rotator.rotateAboutMultipleAxis(
    point=(1, 0, 0), axisAnglePairs=(((0, 0, 1), 90), ((0, 0, 1), 180), ((0, 0, 2), 90)), incrementBy=1)
# last report: At angle 90.0 are at:  +0.0 +0.0i -1.0j +0.0k , makes since!
#
# print("a ", A*B)
# print("b ", B*A)
# print("c ", A/2.0)
# print("d ", B / A)
#
# print((A*A.multiplicativeConjugate()))
#

# rotator.rotate3Dpoint([0, 2, 0], [1, 0, 0], -90, 90)


enc = Encryptor('geoHot.jpeg', 'enc.jpeg', ((1, 7634, 3), 90))
enc.simpleEncryptByQuaternionMult()
