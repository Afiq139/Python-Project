numGrades=int(input('How many grades do you have?: '))
grades=[]
for i in range(0,numGrades,1):
    grade=float(input('Please enter your grade:  '))
    grades.append(grade)
print('Your Grades are: ')
for i in range(0, numGrades,1):
    print(grades[i])
print('Thats all folks')



for mynumber in range(10,21,2):
    print(mynumber)
print('thats all folks')
    
myNumbers=[1,2,3,4,5,6,7,8,9,10]
for myNumber in myNumbers:
    print(myNumber)

print('Thats All Folks')


fruits=['Apple', 'Orange', 'Banana', 'Mango', 'Kiwi']
for fruit in fruits:
    print(fruit)
    for letter in fruit:
        print(letter)
    for l in fruit:
        print(l)

print('Thats All Folks')

print(fruits[0])
print(fruits[1])
print(fruits[1:4]) 
print(fruits[1:5]) 

fruit=fruits[2]
print(fruit)

