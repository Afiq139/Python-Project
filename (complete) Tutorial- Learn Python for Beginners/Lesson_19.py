class students:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    
    def gInput(self,ng):
        self.ng=ng
        self.grades=[]
        for i in range(0,self.ng,1):
            #grd=float(input('Please Enter the grade: '))
            #prompt='Please Enter ' + self.first+"'s Grade: "
            #grd=float(input('Please Enter ' + self.first +"'s Grade = "))
            #grd=float(input(prompt))
            grd=float(input('Please Enter ' + self.first+"'s Grade: "))
            self.grades.append(grd)
        return self.grades
    
    def printGrades(self):
        print(self.first, self.last + "'s Grades are: ")
        for i in range(0,self.ng,1):
            print(self.grades[i])
        print('')
    
    def avGrades(self):
        bucket=0
        for i in range(0,self.ng,1):
            bucket=bucket+self.grades[i]
        avg=bucket/self.ng
        #self.avg=avg
        return avg
    
    def highLow(self):
        highGrade=0
        lowGrade=100
        for i in range(0,self.ng):
            if self.grades[i]>highGrade:
                highGrade=self.grades[i]
            if self.grades[i]<lowGrade:
                lowGrade=self.grades[i]
        return lowGrade,highGrade
        

student1=students('Joe','Evans')
student1.gInput(4)
student2=students('Shirly','Baker')
student2.gInput(6)
print('')
print('Grade Report for ', student1.first, student1.last)
student1.printGrades
print('Average is: ',student1.avGrades())
lowGrade,highGrade=student1.highLow()
print('Low Grade is: ', lowGrade)
print('High Grade is: ', highGrade)
print('')
print('Grade Report for ', student2.first, student2.last)
student2.printGrades
print('Average is: ',student2.avGrades())
lowGrade,highGrade=student2.highLow()
print('Low Grade is: ', lowGrade)
print('High Grade is: ', highGrade)
print('')
print(student1.first, student1.last)
print(student2.first, student2.last)

#testGrades=student1.gInput(4)
#print(testGrades)

student1.printGrades()
avg=student1.avGrades()
print(student1.first +' has an average of', avg)
lowG,highG=student1.highLow()
print(student1.first+' had a high grade of ', highG)
print(student1.first+' had a low grade of ', lowG)
#print(student1.grades)