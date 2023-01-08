# Animating 3D Objects in Vpython


from vpython import *
from time import *

# length=x,width=z,height=y
#floor=box(pos=vector(0,-5,0), length=10, width=10, height=.1, color=color.white)
floor=box(pos=vector(0,-5,0),size=vector(10,.1,10), color=color.white)
ceiling=box(pos=vector(0,5,0),length=10, width=10, height=.1, color=color.white)
backWall=box(pos=vector(0,0,-5),length=10, width=.1, height=10, color=color.white)
leftWall=box(pos=vector(-5,0,0),length=.1, width=10, height=10, color=color.white)
rightWall=box(pos=vector(5,0,0),length=.1, width=10, height=10, color=color.white)
marble=sphere(radius=.75,color=color.red)
deltaX=.1
xpos=0
while True:
    rate(50)
    xpos=xpos+deltaX
    if (xpos>5 or xpos<-5):
        deltaX=deltaX*(-1)
        
    marble.pos=vector(xpos,0,0)
    #pass