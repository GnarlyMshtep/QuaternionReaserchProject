from vpython import *
import Rotator
from visualiserComponents import *
# TO DO
# set up the axis and the canvas to be the way I want it
# set up some styling to make the page un-ugly
# can un-uglify the colors

# define constants:
axisLength = 40  # define the length of each axis
axisRadius = .15  # define the axis radius
RATE = 100
LEGEND = """<bold><large>LEGEND</large></bold>
<span style="color: red;"> The <bold>x</bold> axis is red.</span>
<span style="color: green;"> The <bold>y</bold> axis is green.</span>
<span style="color: blue;"> The <bold>z</bold> axis is blue.</span>

<i>additonal information</i>
<b>Click to toggle between pausing or running.</b>
In GlowScript programs:
- To rotate "camera", drag with right button or Ctrl-drag.
- To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
- On a two-button mouse, middle is left + right.
- To pan left/right and up/down, Shift-drag.
- Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""


# SET UP THE STATIC SCENE STUFF HERE


# set up static html stuff here
scene.append_to_caption(
    """"<style> *{margin : 0; padding: 0; font-family: Times New Roman;}
    canvas{border : 100px solid purple;} """)

# set up the scene
scene = canvas(title="Matan's testing toy", width=800,
               height=450, background=color.black, align="center", color=color.magenta)
scene.center = vec(0, 0, 0)
scene.caption = LEGEND

# I am not using this rn but u can attach some HTML: scene.append_to_caption("""<style>*{background-color : "black"; }</style>""")
"""
xAxis = cylinder(pos=vec(0, 0, -axisLength), axis=vec(
    0, 0, axisLength), radius=axisRadius, color=color.red)
yAxis = cylinder(pos=vec(axisLength, 0, 0), axis=vec(
    axisLength, 0, 0), radius=axisRadius, color=color.green)
zAxis = cylinder(pos=vec(0, axisLength, 0), axis=vec(
    0, axisLength, 0), radius=axisRadius, color=color.blue)
 FOR SOME REASON, THE EXPECTED CONFIGURATION IS BAD and replaced
"""

# create axes, could replace with arrows if I find it critical, x, y and z axis are not as expected
xAxis = curve(pos=[vec(axisLength, 0, 0), vec(-axisLength, 0, 0)],
              color=color.red, radius=axisRadius)
yAxis = curve(pos=[vec(0, axisLength, 0), vec(0, -axisLength, 0)],
              color=color.green, radius=axisRadius)
zAxis = curve(pos=[vec(0, 0, axisLength), vec(0, 0, -axisLength)],
              color=color.blue, radius=axisRadius)

# set up the initial camera position
scene.camera.pos = vec(9.19761, 8.94945, 30.2536)
scene.camera.axis = vec(-4.19761, -3.94946, -11.2501)


# start messing around with rotations and such
ball = rotatingBody(pos=vec(0, 10, 0))
# ball.rotateAboutSingleAxis((1, 0, 0), 0, 90)
sleep(10)
#ball.rotateAboutSingleAxis((7, 1, 5), 0, 165)
print(len(((((3, 0, 2), 100), ((0, 15, 4), 0)), .1, 90)))
ball.rotateAboutMultipleAxis((((3, 0, 2), 60), ((10, 15, 4), -293)), .2)
