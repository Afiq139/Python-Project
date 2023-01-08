numGrades=int(input('How many grades do you have?: '))
grades=[]
bucket=0
for i in range(0,numGrades,1):
    grade=float(input('Please enter your grade:  '))
    grades.append(grade)
print('Your Grades are: ')
for i in range(0, numGrades,1):
    print(grades[i])
for i in range(0, numGrades, 1):
    bucket=+grades[i]
    Average = bucket/numGrades
print('')
print('Your Average is:  ', Average )
print('')
