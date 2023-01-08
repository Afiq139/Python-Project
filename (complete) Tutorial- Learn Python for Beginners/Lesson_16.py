
def tally(x,y):
    z=x+y
    a=23
    b=45
    print('aFun=',a)
    print('bFun=',b)
    return z

def tallys(numnum,myArray):
    tot=0
    for i in range(0,numnum,1):
        tot=tot+myArray[i]
    return tot
    
def tallyss(xy,xz):
    tots=xy+xz
    dif=xy-xz
    prod=xy*xz
    div=xy/xz
    
    return tots, dif, prod, div

def tallysss(numm):
    x=[]
    for i in range(0,numm,1):
        myNum=float(input('Enter Your Number: '))
        x.append(myNum)
    return x
    

    
a=float(input('Please input your first number: '))
b=float(input('Please input your second number: '))
c=tally(a,b)
print('a=',a)
print('b=',b)
print(c)

nums=5
x=[2,4,6,8,10]
e=float(input('Enter first number: '))
f=float(input('Enter second number: '))

t,m,p,v=tallyss(e,f)
print('sum is = ',t)
print('dif is = ',m)
print('product is = ',p)
print('division is = ',v)

mySum=tallys(nums,x)
print('Array total = ', mySum)

numNum=int(input('Enter how many numbers: '))
r=tallysss(numNum)
print(r)

