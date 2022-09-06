class Student:
    def setdata(self):
        self.id = int(input("Enter the id  = "))
        self.name = input("Enter the name = ")
        self.age = int(input("Enter the age = "))

    def display(self):
        print("ID              = ",self.id)
        print("NAME            = ",self.name)
        print("AGE             = ",self.age)

class Marks:
    def setmarks(self):
        self.m1 = int(input("Enter Marks 1 = "))
        self.m2 = int(input("Enter Marks 2 = "))
        self.m3 = int(input("Enter Marks 3 = "))
    
    def cal(self):
        self.total = self.m1+self.m2+self.m3
        self.avg = self.total/3

    def display(self):
        print("MARKS1          = ",self.m1)
        print("MARKS2          = ",self.m2)
        print("MARKS3          = ",self.m3)
        print("TOTAL           = ",self.total)
        print("AVERAGE         = ",self.avg)


class Reportcard(Student,Marks):
    def getgrade(self):
        self.grade=""
        if self.avg >=60 and self.avg<=100:
            self.grade="A"
        elif self.avg>=35 and self.avg<60:
            self.grade="B"
        else:
            self.grade="F"

        print("GRADE           = ",self.grade)

    def display(self):
        Student.display(self)
        Marks.display(self)

r = Reportcard()
r.setdata()
r.setmarks()
r.cal()
r.display()
r.getgrade()


