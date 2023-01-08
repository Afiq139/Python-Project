from time import *
from threading import Thread

def myBox(delayT):
    while True:
        print('.............My Box is open')
        sleep(delayT)
        print('.............My Box is closed')
        sleep(delayT)

def myLED(delayT):
    while True:
        print('My LED is On')
        sleep(delayT)
        print('My LED is off')
        sleep(delayT)

delayBox=5
delayLED=1

boxThread=Thread(target=myBox, args=(delayBox,))
LEDThread=Thread(target=myLED, args=(delayLED,))
boxThread.daemon=True
LEDThread.daemon=True
boxThread.start()
LEDThread.start()

j=0
while True:
    #pass
    print(j)
    j=j+1
    sleep(.1)

#while True:
#   print('My box is open')
#   sleep(5)
#   print('My box is closed')
#   sleep(5)
#   print('My LED is On')
#   sleep(1)
#   print('My LED is off')
#   sleep(1)