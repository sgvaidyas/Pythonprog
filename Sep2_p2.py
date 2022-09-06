class Student:
    def setData(self):
        self.id = int(input("Enter the id = "))
        self.name = input("Enter the name =")
        self.age = int(input("Enter the age ="))

    def display(self):
        print("RECORD  = ")
        print("ID        = ",self.id)
        print("NAME      = ",self.name)
        print("AGE       = ",self.age)

#main function
ob = Student()
ob.setData()
ob.display()


ob1=Student()
Student.setData(ob1)
Student.display(ob1)
