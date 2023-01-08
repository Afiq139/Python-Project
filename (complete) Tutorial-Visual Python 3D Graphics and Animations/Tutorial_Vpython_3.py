# Designing 3D Models with Parameters

from vpython import *
from time import *
mRadius=.75
wallThickness=.1
roomWidth=10
roomDepth=5
roomHeight=10
# length=x,height=y,width=z
floor=box(pos=vector(0,-roomHeight/2,0),size=vector(roomWidth,wallThickness,roomDepth), color=color.white)
ceiling=box(pos=vector(0,roomHeight/2,0),size=vector(roomWidth,wallThickness,roomDepth), color=color.white)
backWall=box(pos=vector(0,0,-roomDepth/2),size=vector(roomWidth,roomHeight,wallThickness), color=color.white)
leftWall=box(pos=vector(-roomWidth/2,0,0),size=vector(wallThickness,roomHeight,roomDepth), color=color.white)
rightWall=box(pos=vector(roomWidth/2,0,0),size=vector(wallThickness,roomHeight,roomDepth), color=color.white)
marble=sphere(radius=mRadius,color=color.red)
deltaX=.1
xpos=0
while True:
    rate(50)
    xpos=xpos+deltaX
    if (xpos>roomWidth/2 or xpos<-roomWidth/2):
        deltaX=deltaX*(-1)
        
    marble.pos=vector(xpos,0,0)
    