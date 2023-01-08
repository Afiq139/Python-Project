class Rectangle:
    def __init__(self,c,L,w):
        self.color=c
        self.length=L
        self.width=w
        x=7
    def area(self):
        self.area=self.length*self.width
        return self.area
    
    def per(self):
        self.perimeter=2*self.length+2*self.width
        return self.perimeter
    
    def diagonal(self):
        self.diag=(self.width**2+self.length**2)**(1/2)
        return self.diag
    
    def volume(self,h):
        self.height=h
        self.vol=self.length*self.width*self.height
        return self.vol
        
        

# myRect1=Rectangle(color,length,width)
myRect1=Rectangle('red',2,1)

print('Color is: ',myRect1.color)
print('Length is: ',myRect1.length)
print('Width is: ',myRect1.width)
print('Area is: ',myRect1.area())
print('Perimeter is: ',myRect1.per())
print('Volume is: ',myRect1.volume(10))

a= 4
b= 3

myRect2=Rectangle('blue',a,b)

print('Your Diagonal is: ', myRect2.diagonal())
print('first diagonal is: ', myRect1.diagonal())
print(myRect1.color)
print('myRect1 length = ',myRect1.length)
#area=myRect1.area()
#print('myRect1 Area = ',myRect1.area())
#print('myRect1 Area = ',area)
print(myRect2.color)
print('myRect2 length = ',myRect2.length)
print('myRect1 diagonal = ', myRect1.diagonal())
myVol=myRect1.volume(10)
print('myRect1 volume = ', myVol)