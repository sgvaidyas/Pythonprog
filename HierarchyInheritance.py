class Shape:
    def __init__(self):
        self.leng = 0
        self.bred = 0
        self.rad = 0

    def setlen(self):
        self.leng = float(input("Enter the length = "))

    def setbred(self):
        self.bred = float(input("Enter the breadth = "))
      
    def setrad(self):
        self.rad = float(input("Enter the radius = "))


class Square(Shape):
    def __init__(self):
        self.area = 0
        self.peri = 0

    def cal(self):
        self.area = self.leng**2
        self.peri = 4*self.leng

    def display(self):
        print("LENGTH      = ", self.leng)
        print("AREA        = ", self.area)
        print("PERIMETER   = ", self.peri)


class Circle(Shape):
    def __init__(self):
        self.area = 0
        self.circum = 0

    def cal(self):
        self.area = 3.142 * self.rad*self.rad
        self.circum = 2*3.142 * self.rad

    def display(self):
        print("RADIUS          = ", self.rad)
        print("AREA            = ", self.area)
        print("CIRCUMFERENCE   = ", self.circum)

c = Circle()
c.setrad()
c.cal()
c.display()
print("------------------")
ob = Square()
ob.setlen()
ob.cal()
ob.display()


