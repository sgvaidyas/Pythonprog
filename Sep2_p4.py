class Employee:
    #parameterized init function
    def __init__(self,eid,name,sal):
        self.empId = eid
        self.empName = name
        self.empSal = sal

    def display(self):
        print("RECORD__________________")
        print("EMP ID     = ",self.empId)
        print("EMP NAME   = ",self.empName)
        print("EMP SAL    = ",self.empSal)

#main
ob = Employee(111,'shilpa',9999.90)
ob.display()

