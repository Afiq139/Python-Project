#Three Dimensional Clock Face Model in Vpython

from vpython import *
import numpy as np
clockR=2                             #clock Radius
clockT=clockR/10                     #clock thickness
majorTickL=clockR/7                  #major tick length
majorTickT=2*np.pi*clockR/400        #major tick thickness
majorTickw=clockT*1.2                #Major tick width


minorTickL=clockR/12                  #minor tick length
minorTickT=2*np.pi*clockR/600        #minor tick thickness
minorTickw=clockT*1.2                #Minor tick width

for theta in np.linspace(0,2*np.pi,13):
    majorTick=box(axis=vector(clockR*np.cos(theta),clockR*np.sin(theta),0), color=color.black, length=majorTickL, width=majorTickw, height=majorTickT, pos=vector((clockR-majorTickL/2)*np.cos(theta),(clockR-majorTickL/2)*np.sin(theta),0))

for theta in np.linspace(0,2*np.pi,61):
    minorTick=box(axis=vector(clockR*np.cos(theta),clockR*np.sin(theta),0), color=color.black, length=minorTickL, width=minorTickw, height=minorTickT, pos=vector((clockR-minorTickL/2)*np.cos(theta),(clockR-minorTickL/2)*np.sin(theta),0))

clockFace=cylinder(axis=vector(0,0,1), color=vector(0,1,.8), length=clockT, radius=clockR, pos=vector(0,0,-clockT/2))
while True:
    pass


