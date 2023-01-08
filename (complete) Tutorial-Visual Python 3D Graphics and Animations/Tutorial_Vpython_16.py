#Modeling a 3D Analog Clock in Vpython

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

minuteHandL=clockR-majorTickL    #minute Hand Length
minuteHandT=minuteHandL/25  #minute Hand Thickness
minuteHandOffset=clockT/2+minuteHandT     #minute offset

hourHandL=.75*minuteHandL    #Hour Hand Length
hourHandT=minuteHandT*1.5  #Hour Hand Thickness
hourHandOffset=clockT+hourHandT     #hour offset

secondHandL=clockR-majorTickL/2    #second Hand Length
secondHandT=minuteHandL/50  #second Hand Thickness
secondHandOffset=clockT*1.5+minuteHandT     #second offset

hubRadius=clockT/2 #hub radius

hourAngle=np.pi/2
minuteAngle=np.pi/2
minInc=.0001
hourInc=minInc/12
secondAngle=np.pi/2
secondInc=minInc*60


for theta in np.linspace(0,2*np.pi,13):
    majorTick=box(axis=vector(clockR*np.cos(theta),clockR*np.sin(theta),0), color=color.black, length=majorTickL, width=majorTickw, height=majorTickT, pos=vector((clockR-majorTickL/2)*np.cos(theta),(clockR-majorTickL/2)*np.sin(theta),0))

for theta in np.linspace(0,2*np.pi,61):
    minorTick=box(axis=vector(clockR*np.cos(theta),clockR*np.sin(theta),0), color=color.black, length=minorTickL, width=minorTickw, height=minorTickT, pos=vector((clockR-minorTickL/2)*np.cos(theta),(clockR-minorTickL/2)*np.sin(theta),0))

clockFace=cylinder(axis=vector(0,0,1), color=vector(0,1,.8), length=clockT, radius=clockR, pos=vector(0,0,-clockT/2))
minuteHand=arrow(axis=vector(0,1,0), color=color.red, shaftwidth=minuteHandT, length=minuteHandL, pos=vector(0,0,minuteHandOffset))
hourHand=arrow(axis=vector(0,1,0), color=color.red, shaftwidth=hourHandT, length=hourHandL, pos=vector(0,0,hourHandOffset))
secondHand=arrow(axis=vector(0,1,0), color=color.red, shaftwidth=secondHandT, length=secondHandL, pos=vector(0,0,secondHandOffset))
#hub=sphere(color=color.red, radius=hubRadius)
hub=cylinder(axis=vector(0,0,1), color=color.red, radius=hubRadius, length=2*clockT)


while True:
    rate(18)
    hourAngle=hourAngle-hourInc
    minuteAngle=minuteAngle-minInc
    secondAngle=secondAngle-secondInc

    hourHand.axis=vector(hourHandL*np.cos(hourAngle),hourHandL*np.sin(hourAngle),0)
    minuteHand.axis=vector(minuteHandL*np.cos(minuteAngle),minuteHandL*np.sin(minuteAngle),0)
    secondHand.axis=vector(secondHandL*np.cos(secondAngle),secondHandL*np.sin(secondAngle),0)
    #pass

#>>>import time
#>>>print(time.time())
#output:1650977807.809178
#>>>myTime=time.localtime(time.time())
#>>>print(myTime)
#output: time.struct_time(tm_year=2022, tm_mon=4, tm_mday=26, tm_hour=21, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=116, tm_isdst=0)
#myTime[3] //array
