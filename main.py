from PolarQuaternion import PolarQuaternion
from Quaternion import Quaternion
import Rotator as rotator

A = Quaternion(0, 3, 4, 0)
B = Quaternion(0, 0, 5, 2)


print("a ", A*B)
print("b ", B*A)
print("c ", A/2.0)
print("d ", B / A)

print((A*A.multiplicativeConjugate()))


#rotator.rotate3Dpoint([0, 2, 0], [1, 0, 0], -90, 90)
