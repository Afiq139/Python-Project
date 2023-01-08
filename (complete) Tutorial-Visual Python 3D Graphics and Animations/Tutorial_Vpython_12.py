# Understanding Orientation and Axis Parameters

from vpython import *
import numpy as np
arrowL=2  #arrow length
arrowT=.02 #arrow thickness
Theta=np.pi/4 #Angle in Radian

Xarrow=arrow(axis=vector(1,0,0), color=color.red, Length=arrowL,shaftwidth=arrowT)
Yarrow=arrow(axis=vector(0,1,0), color=color.green, Length=arrowL,shaftwidth=arrowT)
zarrow=arrow(axis=vector(0,0,1),color=color.blue,Length=arrowL,shaftwidth=arrowT)
pntArrow=arrow(axis=vector(np.cos(Theta),np.sin(Theta), 0), color=color.orange, Length=arrowL, shaftwidth=arrowT)

while True:
    for myAngle in np.linspace(0,2*np.pi,1000):
        rate(50)
        pntArrow.axis=vector(np.cos(myAngle),np.sin(myAngle),0)
        

    pass