# Program for Orb With Continuously Varying Color Rainbow

from vpython import *
myOrb=sphere(radius=1, color=color.white)
rchan=0
gchan=0
bchan=0
rInc=.001
gInc=.002
bInc=.0015
while True:
    rate(500)
    rchan=rchan+rInc
    gchan=gchan+gInc
    bchan=bchan+bInc
    myOrb.color=vector(rchan,gchan,bchan)
    if rchan>=1 or rchan<=0:
        rInc=rInc*(-1)
    if rchan>=1 or gchan>=0:
        gInc=gInc*(-1)
    if bchan>=1 or bchan<=0:
        bInc=rInc*(-1)