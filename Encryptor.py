from Quaternion import Quaternion
import Rotator
from random import randbytes, randint
import numpy
import struct

"""
MANIFESTO:
this will be the encryptor class: it will take a file to encrypt and what to call the file it is going to write to.
It will have several encryption techniques, all quaternion based
- it uses the rotator module, but doesn't inherit from anything
- preformence is, at best, lightly considered
"""
"""
Look into:
    il module, inline asm.
    writing this as a c program or something
    just don't let python do heavy lifting!
"""
MINCONSTANT = -100
MAXCONSTANT = 100


def getRandomAxisAnglePair():  # maybe a good way to ask for a more random number
    return ((randint(MINCONSTANT, MAXCONSTANT), randint(MINCONSTANT, MAXCONSTANT),
             randint(MINCONSTANT, MAXCONSTANT)), randint(MINCONSTANT, MAXCONSTANT))


class Encryptor:
    def __init__(self, fromFile: str, toFile: str, axisAnglePair=None) -> Quaternion:
        """
        example init:
            Encryptor('hotz.jpeg', 'encHotz.jpg', ((1,2,6), 90 ))
                    *fileToEncrypt**fileToWriteTo**AxisAndAngleInDeg**
        """
        self.fromFile = fromFile
        self.toFile = toFile
        if axisAnglePair == None:
            self.axisAnglePair = getRandomAxisAnglePair()

        else:
            self.axisAnglePair = axisAnglePair
        self.extraneousBytes = 0
        self.keyQuaternion = Quaternion(
            False, vec=axisAnglePair[0], theta=axisAnglePair[1])
        # could have it write out key to file (in case we forget or whatever)

    # this is certainely not the most efficient way (converting to list, didn't want to deal with ndarray)

    def readBytesFromFile(self):  # returns a list of file bytes as ints
        bytesRead = []
        with open(self.fromFile, mode='rb') as file:  # b is important -> binary
            bytesRead = file.read()
        file.close()
        return list(bytesRead)

    def writeBytesToFile(self, bytes):
        with open(self.toFile, mode="wb") as wfile:
            wfile.write(bytes)
        wfile.close()

    def simpleEncryptAsRotated3DPoint(self):
        Tuple_Size = 3  # the tuple size used for this method
        encryptedData = []
        data = self.readBytesFromFile()
        # ammend list to len(list)%==0 (we can have exactly N 4-tuples)
        while len(data) % Tuple_Size > 0:
            self.extraneousBytes += 1
            data.append(randbytes(1))
        # encrypt here
        for i in range(int(len(data)/Tuple_Size)):
            encryptedData += Rotator.rotate3DpointFromToAngle(
                (data[i], data[i+1], data[i+2]), self.axisAnglePair[0], self.axisAnglePair[1], self.axisAnglePair[1], 1)['QuaternionAsList']
        # problem: I'm encrypting 3 points and getting back 4

        print(encryptedData)

    def simpleEncryptByQuaternionMult(self):
        Tuple_Size = 3  # the tuple size used for this method
        encryptedData = []
        data = self.readBytesFromFile()
        # ammend list to len(list)%==0 (we can have exactly N 4-tuples)
        while len(data) % Tuple_Size > 0:
            self.extraneousBytes += 1
            data.append(randbytes(1))
        # encrypt here
        for i in range(int(len(data)/Tuple_Size)):
            encryptedData += (Quaternion(True, r=0, x=data[i],
                                         y=data[i+1], z=data[i+2]) * self.keyQuaternion).getQuaternionAsList()
        # problem: I'm encrypting 3 points and getting back 4
        encryptedData = [round(el) % 256 for el in encryptedData]
        print(encryptedData)
        self.writeBytesToFile(encryptedData)

    """
    def simpleKeyEncryptFile(self):
        intData = numpy.fromfile(self.fromFile, '<i8', -1).tolist()

        numsAppended = 0
        # make sure our array has tuples of 3 to fill out our points (prob can feel with 0s since I'm just gonna ommit these later)
        for i in range(0, len(intData) % 3):
            intData.append(randint(MINCONSTANT, MAXCONSTANT))
            numsAppended += 1

        # qtData = numpy.ndarray(1, Quaternion, buffer=(Quaternion(
         #   True, r=intData[i], x=intData[i+1], y=intData[i+2], z=intData[i+3]) for i in range(len(intData)/4)))

        # encryptedData = numpy.ndarray((Rotator.rotate3DpointFromToAngle(
           # (intData[i], intData[i+1], intData[i+2]), self.axisAnglePair[0], self.axisAnglePair[1], self.axisAnglePair[2]) for i in range(int(len(intData)/3))))

        binaryData = bytearray(intData)
        f = open(self.toFile, 'w+b')
        f.write(binaryData)
        f.close
    """