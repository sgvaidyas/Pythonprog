class Employee:
    def setdata(self):
        isValid = True
        try:
            self.empId = int(input("Enter the id = "))
            self.empName = input("Enter the name = ")
            self.empSal = float(input("Enter the sal = "))
        except:
            print("Enter the data Id=int,name=string and sal=float")
            isValid = False
        
        print()
        return isValid

    def display(self):
        print("=================================")
        print("ID            =  ",self.empId)
        print("NAME          =  ",self.empName)
        print("SALARY        =  ",self.empSal)


n = int(input("Enter the number of records = "))
recs = []
for i in range(n):
    ob = Employee()
    valid = ob.setdata()
    while valid==False:
        print("Re-enter the data")
        valid = ob.setdata()
    print("---------Data successfully entered----------")
    recs.append(ob)

print("All the records = ")
for i in range(n):
    recs[i].display()

