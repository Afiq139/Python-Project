numGrades=int(input('How many grades do you have?: '))
grades=[]
bucket=0
lowGrade=100
highGrade=0

for i in range(0,numGrades,1):
    grade=float(input('Please enter your grade:  '))
    grades.append(grade)
print('')
print('Your Grades are: ')
for i in range(0, numGrades,1):
    print(grades[i])
for i in range(0, numGrades, 1):
    bucket=+grades[i]
    Average = bucket/numGrades
print('')
print('Your Average is:  ', Average )
for i in range(0, numGrades,1):
    if grades[i]<lowGrade:
        lowGrade=grades[i]
print('Your Low Grade is:  ', lowGrade)
for i in range(0, numGrades,1):
    if grades[i]>highGrade:
        highGrade=grades[i]
print('Your High Grade is:  ', highGrade)
print('')

for i in range(0,numGrades-1, 1):
    for i in range(0,numGrades-1, 1):
        if grades[i]<grades[i+1]:
            swp=grades[i]
            grades[i]=grades[i+1]
            grades[i+1]=swp     
print('Your sorted Grade List is:  ')

for i in range(0,numGrades,1):
    print(grades[i])
print('')
       