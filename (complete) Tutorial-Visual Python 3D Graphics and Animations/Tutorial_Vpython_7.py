# Vpython Model of a Thermometer

from vpython import *
import numpy as np
glassBulb=sphere(radius=1.25, color=color.white, opacity=.3)
glassCyl=cylinder(radius=.65, length=6, color=color.white, opacity=.3)
mercSphere=sphere(radius=1,color=color.red)
mercColumn=cylinder(radius=.45, length=6, color=color.red)

for tick in np.linspace(1,6,15):
    box(size=vector(.1,.5,.25),color=color.white, pos=vector(tick,0,.5))
    
while True:
    #pass 
    for myTemp in np.linspace(1,6,100):
        rate(100)
        mercColumn.length=myTemp
    for myTemp in np.linspace(6,1,100):
        rate(100)
        mercColumn.length=myTemp
    