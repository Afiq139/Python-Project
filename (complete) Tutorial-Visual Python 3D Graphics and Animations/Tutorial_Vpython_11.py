#improved color orb with Constant Brightness

from vpython import *
myOrb=sphere(radius=1, color=vector(1,1,0))
rchan=1       #red channel
gchan=1       #green channel
bchan=0       #blue channel
rInc=.001     #red increment
gInc=-.001    #green increment
bInc=.001     #blue increment

while True:
    rate(250)
    rchan=rchan+rInc
    gchan=gchan+gInc
    bchan=bchan+bInc
    
    if rchan<=1:
        rApply=rchan
    if rchan>1:
        rApply=1
        
    if gchan<=1:
        gApply=gchan
    if gchan>1:
        gApply=1
    
    if bchan<=1:
        bApply=bchan
    if bchan>1:
        bApply=1
    
    myOrb.color=vector(rApply,gApply,bApply)
    
    if rchan>=1.5 or rchan<=0:
        rInc=rInc*(-1)
        
    if gchan>=1.5 or gchan<=0:
        gInc=gInc*(-1)
    
    if bchan>=1.5 or bchan<=0:
        bInc=bInc*(-1)  
    
    print(rApply+gApply+bApply)
    
    
    
    
    