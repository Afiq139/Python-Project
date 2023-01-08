def inputGrades(nm):
    grades=[]
    for i in range(0,nm,1):
        grd=float(input('Please enter your grade: '))
        grades.append(grd)
    return grades

def printGrades(nm,x):
    for i in range(0,nm,1):
        print(x[i])

def averageGrades(nm,x):
    tot=0
    for i in range(0,nm,1):
        tot=tot+x[i]
    average=tot/nm
    return average    

def highLow(nm,x):
    highG=0
    lowG=100
    for i in range(0,nm,1):
        if(x[i]<lowG):
            lowG=x[i]
        if(x[i]>highG):
            highG=x[i]
    return highG, lowG
        
    
numGrades=int(input('How many grades? '))
myGrades=inputGrades(numGrades)
print('')
print('Your Grades are: ')
printGrades(numGrades, myGrades)
print('')
avg=averageGrades(numGrades,myGrades)
print('Your average is: ', round(avg,1))

highG,lowG=highLow(numGrades,myGrades)
print('Your high grades is: ', highG)
print('Your low grades is: ', lowG)