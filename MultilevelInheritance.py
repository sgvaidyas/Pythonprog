class A:
    def setA(self):
        self.valA = int(input("Enter data A = "))
    def displayA(self):
        print("A = ",self.valA)

class B(A):
    def setB(self):
        self.valB = int(input("Enter data B = "))
    def displayB(self):
        print("B = ",self.valB)

class C(B):
    def setC(self):
        self.valC = int(input("Enter data C = "))
    def displayC(self):
        print("C = ",self.valC)


c = C()
c.setA()
c.setB()
c.setC()
c.displayA()
c.displayB()
c.displayC()

