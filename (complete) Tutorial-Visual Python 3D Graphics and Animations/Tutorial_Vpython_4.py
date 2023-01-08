# Understanding 3D Graphic Parameters

from vpython import *
from time import *
mRadius=2
wallThickness=1
roomWidth=15
roomDepth=15
roomHeight=8
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
    rate(50) #speed
    xpos=xpos+deltaX
    Xrme=xpos+mRadius  #x-direction in right marble edge
    Xlme=xpos-mRadius  #x-direction in left marble edge
    Rwe=roomWidth/2-wallThickness/2   #rightWall Edge
    Lwe=-roomWidth/2+wallThickness/2   #leftwall Edge
    
    if (Xrme>Rwe or Xlme<Lwe):
        deltaX=deltaX*(-1)
        
    marble.pos=vector(xpos,0,0)
    