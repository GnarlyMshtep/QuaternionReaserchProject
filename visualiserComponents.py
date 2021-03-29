from vpython import *
import Rotator

RATE = 80


class rotationAxisAndCaption:
    """display error axis and the degrees of rotation, delete after rotation is done"""

    def __init__(self, **kargs):
        self.graphic = arrow(
            pos=vec(0, 0, 0), axis=vec(kargs["axis"][0], kargs["axis"][1], kargs["axis"][2]).hat*8, color=color.purple, visible=True, shaftWidth=6)
        self.captionIncluded = kargs.get("caption")
        if(self.captionIncluded):
            self.text = label(
                text=kargs["caption"], pos=self.graphic.axis,
                xoffset=70, yoffset=70, space=30,
                height=16, border=4,
                font='sans')

    def deleteInternals(self):
        self.graphic.visible = False
        if (self.captionIncluded):
            self.caption.visible = False
            del self.caption
        del self.graphic


class rotatingBody:
    """a rotating body is a quaternion-rotation object with a graphics component. All Computaiton is carried through it"""

    def __init__(self, **kargs):
        self.graphic = sphere(pos=kargs.get("pos") or vec(6, 0, 0), radius=kargs.get("radius") or .9,
                              color=kargs.get("color") or color.orange, visible=True)

    def rotateAboutSingleAxis(self, axis: list, fromAngle: degrees = 0, toAngle: degrees = 90, incrementBy: degrees = .5):
        positions = Rotator.rotate3DpointFromToAngle(
            (self.graphic.pos.x, self.graphic.pos.y, self.graphic.pos.z), axis, fromAngle, toAngle, incrementBy)  # get all positions along the rotation
        # change ball position ot every one of positions along path

        rAxis = rotationAxisAndCaption(
            axis=axis, caption=f"rotate by {toAngle} about {axis}")

        for position in positions["list of positions"]:
            rate(RATE)
            self.graphic.pos = vec(position[0], position[1], position[2])
            #print(scene.camera.axis, scene.camera.pos)
        rAxis.deleteInternals()
        del rAxis
