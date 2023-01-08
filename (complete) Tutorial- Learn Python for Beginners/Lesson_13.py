print('It is Time to Count!')
j=1.0
while(j<=10):
    print(j)
    j=j+.1
    j=round(j,1)
print('thats All Folks')

print('')

numGrades=int(input('How many Grades do you have? '))
j=0
grades=[]
while (j<numGrades):
    grd=float(input('Please Input Your Grades: '))
    grades.append(grd)
    j=j+1
j=0
while (j<numGrades):
    print(grades[j])
    j=j+1
print('Thats all Folks!')

