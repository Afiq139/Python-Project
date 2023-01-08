# Animating 3D Objects by Changing Dimensions in Visual Python 

from vpython import *
import numpy as np
#Piston1=cylinder(radius=1, length=3, color=color.red, opacity=.5)
mySphere=sphere(radius=1, color=color.red, opacity=.5)
while True:
    #for myLength in range(1,6,1):
    #for myLength in np.linspace(1,6,100):
    #for myOpacity in np.linspace(1,0,100):
    for myRadius in np.linspace(.1,1,100):
        rate(250)
        #Piston1.length=myLength
        #Piston1.opacity=myOpacity
        mySphere.radius=myRadius
        
        
    #for myLength in range(6,1,-1):
    #for myLength in np.linspace(6,1,100):
    #for myOpacity in np.linspace(0,1,100):
    for myRadius in np.linspace(1,.1,100):
        rate(250)   
        #Piston1.length=myLength
        #Piston1.opacity=myOpacity
        mySphere.radius=myRadius   

