# Understanding and using widgets in Vpython

from cProfile import run
from tkinter import BaseWidget
from zlib import Z_BEST_COMPRESSION
from vpython import *
from time import *
mRadius=.5
wallThickness=.1
roomWidth=12
roomDepth=20
roomHeight=15
# length=x,height=y,width=z
floor=box(pos=vector(0,-roomHeight/2,0),size=vector(roomWidth,wallThickness,roomDepth), color=color.white)
ceiling=box(pos=vector(0,roomHeight/2,0),size=vector(roomWidth,wallThickness,roomDepth), color=color.white)
backWall=box(pos=vector(0,0,-roomDepth/2),size=vector(roomWidth,roomHeight,wallThickness), color=color.white)
leftWall=box(pos=vector(-roomWidth/2,0,0),size=vector(wallThickness,roomHeight,roomDepth), color=color.white)
rightWall=box(pos=vector(roomWidth/2,0,0),size=vector(wallThickness,roomHeight,roomDepth), color=color.white)
marble=sphere(radius=mRadius,color=color.purple)

deltaX=.1
deltaY=.1
deltaZ=.1

xpos=0
ypos=0
zpos=0
run=0
myspeed=1

def ballColorRed(x):
    marble.color=color.red

button(bind=ballColorRed, text='Red', color=color.black, background=color.red)

def ballColorGreen(x):
    marble.color=color.green

button(bind=ballColorGreen, text='Green', color=color.black, background=color.green)

def ballColorBlue(x):
    marble.color=color.blue

button(bind=ballColorBlue, text='Blue', color=color.black, background=color.blue)

scene.append_to_caption('\n\n')

def ballOpacity(x):
    op=x.value
    marble.opacity=op

wtext(text='Choose Ball Opacity')


slider(bind=ballOpacity, vertical=False, min=0, max=1, value=1, text='Opacity of Ball')

scene.append_to_caption('\n\n')

def speed(x):
    global myspeed
    if x.selected=='1':
        myspeed=1
    if x.selected=='2':
        myspeed=2
    if x.selected=='3':
        myspeed=3
    if x.selected=='4':
        myspeed=4
    if x.selected=='5':
        myspeed=5
    
wtext(text='Ball Speed')
scene.append_to_caption('       ')

menu(bind=speed, choices=['1','2','3','4','5'])

scene.append_to_caption('\n\n')

def runRadio(x):
    print(x.checked)
    global run
    if x.checked==True:
        run=1
    if x.checked==False:
        run=0

radio(bind=runRadio,text='Run') #radio button

scene.append_to_caption('       ')

def bigBall(x):
    global mRadius
    if x.checked==True:
        mRadius=mRadius*2
        marble.radius=mRadius


    if x.checked==False:
        mRadius=mRadius/2
        marble.radius=mRadius


checkbox(bind=bigBall,text='Big Ball') 

while True:
    rate(50) #speed
    
    xpos=xpos+deltaX*run*myspeed
    ypos=ypos+deltaY*run*myspeed
    zpos=zpos+deltaZ*run*myspeed
    
    Xrme=xpos+mRadius  #x-direction in right marble edge
    Xlme=xpos-mRadius  #x-direction in left marble edge
    Ytme=ypos+mRadius  #y-direction of top marble edge
    Ybme=ypos-mRadius  #y-direction of bottom marble edge
    Zbme=zpos-mRadius  #z-direction of bottom marble edge     
    Zfme=zpos+mRadius  #z-direction of front marble edge
    
    Rwe=   roomWidth/2-wallThickness/2      #rightWall Edge
    Lwe=  -roomWidth/2+wallThickness/2     #leftwall Edge
    Cwe=   roomHeight/2-wallThickness/2      #Ceiling Wall Edge
    Flwe= -roomHeight/2+wallThickness/2     #Floor Wall Edge
    Bwe=  -roomDepth/2+wallThickness/2     #Back Wall Edge
    Frwe=  roomDepth/2-wallThickness/2     #Front Wall Edge
    
    
    if (Xrme>=Rwe or Xlme<=Lwe):
        deltaX=deltaX*(-1)
        
    if (Ytme>=Cwe or Ybme<=Flwe):
        deltaY=deltaY*(-1)
        
    if (Zfme>=Frwe or Zbme<=Bwe):
        deltaZ=deltaZ*(-1)
              
    marble.pos=vector(xpos,ypos,0)