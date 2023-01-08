# NonBlocking Dual Animations in Vpython

from vpython import *
myCylOrange=cylinder(radius=1,color=color.orange,length=6)
myCylCyan=cylinder(radius=1, length=6, color=color.cyan,pos=vector(0,3,0))
myCylOrangeLength=1
myCylCyanLength=1
myCylOrangeDelta=.01
myCylCyanDelta=.02

while True:
    rate(50)
    myCylOrangeLength=myCylOrangeLength+myCylOrangeDelta
    myCylCyanLength=myCylCyanLength+myCylCyanDelta
    myCylOrange.length=myCylOrangeLength
    myCylCyan.length=myCylCyanLength
    if myCylOrangeLength>=6 or myCylOrangeLength<=.1:
        myCylOrangeDelta=myCylOrangeDelta*(-1)
    if myCylCyanLength>=6 or myCylCyanLength<=.1:
        myCylCyanDelta=myCylCyanDelta*(-1)
        
    
    
