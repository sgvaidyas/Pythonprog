class Rectangle:
    #init function acts like constructor-> called automatically
    #when the object is created (and is called only once)
    def __init__(self):
        self.leng = 2
        self.bread = 2

    def setData(self):
        self.leng = float(input("Enter the length = "))
        self.bread = float(input("Enter the breadth = "))

    def calculate(self):
        self.area = self.leng*self.bread
        self.peri = 2*(self.leng+self.bread)


    def display(self):
        print("LENGTH       = " ,self.leng)
        print("BREADTH      = " ,self.bread)
        print("AREA         = " ,self.area)
        print("PERIMETER    = " ,self.peri)

#main
ob = Rectangle()
ob.calculate()
ob.display()
ob.setData()
ob.calculate()
ob.display()




