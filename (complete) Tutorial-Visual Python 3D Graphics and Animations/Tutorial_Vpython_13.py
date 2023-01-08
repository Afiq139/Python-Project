# Understanding Orientation in Three Dimensional Parameter Space


from vpython import *
import numpy as np

arrowL=2 #arrow length
arrowT=.02 #arrow thickness
pntT=.02  #pointer thickness
bradius=.05 #ball radius

xarrow=arrow(axis=vector(1,0,0), color=color.red, Length=arrowL, shaftwidth=arrowT)
yarrow=arrow(axis=vector(0,1,0), color=color.green, Length=arrowL, shaftwidth=arrowT)
Zarrow=arrow(axis=vector(0,0,1), color=color.blue, Length=arrowL, shaftwidth=arrowT)
Parrow=arrow(axis=vector(1,0,0), color=color.orange,shaftwidth=pntT)
myBall=sphere(make_trail=True,trail_color=color.orange, radius=bradius,color=color.red, pos=vector(1,0,0))
while True:
    for myAngle in np.linspace(0,2*np.pi,1000):
        rate(200)
        Parrow.axis=vector(np.cos(myAngle),np.sin(myAngle),0)
        #Parrow.length=arrowL
        myBall.pos=vector(np.cos(myAngle),np.sin(myAngle),0)

    for myAngle in np.linspace(0,5*np.pi/2,1000):
        rate(200)
        Parrow.axis=vector(np.cos(myAngle),0,np.sin(myAngle))
        #Parrow.length=arrowL
        myBall.pos=vector(np.cos(myAngle),0,np.sin(myAngle))
    

    for myAngle in np.linspace(0,2*np.pi,1000):
        rate(200)
        Parrow.axis=vector(0,np.sin(myAngle),np.cos(myAngle))
        #Parrow.length=arrowL
        myBall.pos=vector(0,np.sin(myAngle),np.cos(myAngle))

    for myAngle in np.linspace(np.pi/2,2*np.pi,1000):
        rate(200)
        Parrow.axis=vector(np.cos(myAngle),0,np.sin(myAngle))
        #Parrow.length=arrowL
        myBall.pos=vector(np.cos(myAngle),0,np.sin(myAngle))

        