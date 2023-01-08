# Bouncing Ball Simulation in Visual Python

from tkinter import BaseWidget
from zlib import Z_BEST_COMPRESSION
from vpython import *
from time import *
mRadius=.5
wallThickness=.1
roomWidth=12
roomDepth=20
roomHeight=2
# length=x,height=y,width=z
floor=box(pos=vector(0,-roomHeight/2,0),size=vector(roomWidth,wallThickness,roomDepth), color=color.white)
ceiling=box(pos=vector(0,roomHeight/2,0),size=vector(roomWidth,wallThickness,roomDepth), color=color.white)
backWall=box(pos=vector(0,0,-roomDepth/2),size=vector(roomWidth,roomHeight,wallThickness), color=color.white)
leftWall=box(pos=vector(-roomWidth/2,0,0),size=vector(wallThickness,roomHeight,roomDepth), color=color.white)
rightWall=box(pos=vector(roomWidth/2,0,0),size=vector(wallThickness,roomHeight,roomDepth), color=color.white)
marble=sphere(radius=mRadius,color=color.red)

deltaX=.1
deltaY=.1
deltaZ=.1

xpos=0
ypos=0
zpos=0

while True:
    rate(50) #speed
    
    xpos=xpos+deltaX
    ypos=ypos+deltaY
    zpos=zpos+deltaZ
    
    Xrme=xpos+mRadius  #x-direction in right marble edge
    Xlme=xpos-mRadius  #x-direction in left marble edge
    Ytme=ypos+mRadius  #y-direction of top marble edge
    Ybme=ypos-mRadius  #y-direction of bottom marble edge
    Zbme=zpos-mRadius  #z-direction of bottom marble edge     
    Zfme=zpos+mRadius  #z-direction of front marble edge
    
    Rwe=   roomWidth/2-wallThickness/2      #rightWall Edge
    Lwe=  -roomWidth/2+wallThickness/2     #leftwall Edge
    Cwe=   roomHeight/2-wallThickness/2      #Ceiling Wall Edge
    Flwe= -roomHeight/2+wallThickness/2     #Floor Wall Edge
    Bwe=  -roomDepth/2+wallThickness/2     #Back Wall Edge
    Frwe=  roomDepth/2-wallThickness/2     #Front Wall Edge
    
    
    if (Xrme>=Rwe or Xlme<=Lwe):
        deltaX=deltaX*(-1)
        
    if (Ytme>=Cwe or Ybme<=Flwe):
        deltaY=deltaY*(-1)
        
    if (Zfme>=Frwe or Zbme<=Bwe):
        deltaZ=deltaZ*(-1)
              
    marble.pos=vector(xpos,ypos,0)