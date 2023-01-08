import pickle
with open('studentData.pkl', 'rb') as DataF:
   numStudents=pickle.load(DataF)
   names=pickle.load(DataF)
   grades=pickle.load(DataF)
print(numStudents)
print(names)
print(grades)

while(1==1):  
    name=input('Which Student do you want to check? ')
    for i in range(0, numStudents, 1):
        if (names[i]==name):
            print(str(name)+"'s grade is "+str(grades[i])+'.')