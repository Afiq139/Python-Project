myNum=float(input('Please Input Your Number: '))
rem=myNum%2
if (myNum>0 and rem==0):
    print('You have an Even Positive Number')
if (myNum>0 and rem==1):
    print('You have an Odd Positive Number')
if (myNum<0 and rem==0):
    print('You have an Even Negative Number')
if (myNum<0 and rem==1):
    print('You have an Odd Negative Number')
if (myNum==0):
    print('Your Number is Zero')
    
    