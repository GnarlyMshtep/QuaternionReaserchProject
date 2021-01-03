from Quaternion import Quaternion
import Rotator as Rotator
from MatansFrange import frange

#print(frange(90, 180, .333))

A = Quaternion(True, r=0.42, x=.68, y=.33, z=.5)
B = Quaternion(False, theta=65, vec=[.75, .36, .55])

#print(A, B)

rotator = Rotator.rotate3Dpoint((1, 0, 0), (0, 0, 1), 0, 180, 1)

#
# print("a ", A*B)
# print("b ", B*A)
# print("c ", A/2.0)
# print("d ", B / A)
#
# print((A*A.multiplicativeConjugate()))
#

# rotator.rotate3Dpoint([0, 2, 0], [1, 0, 0], -90, 90)
