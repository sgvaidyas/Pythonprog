class A:
    def __init__(self,a,b):
        self.valA = a
        self.valB = b

    def disp(self):
        print("A = ",self.valA)
        print("B = ",self.valB)


class B(A):
    def __init__(self,a,b,c):
        #A.__init__(self,a,b)
        super().__init__(a,b)
        self.valc = c

    def disp(self):
        super().disp()
        print("C = ",self.valc)

class D(B):
    def __init__(self,a,b,c,d):
        super().__init__(a,b,c)
        self.vald = d

    def disp(self):
        super().disp()
        print("D = ",self.vald)
        

ob1 = D(11,22,33,44)
ob1.disp()



'''
ob = A(22,33)
ob.dispA()
'''
