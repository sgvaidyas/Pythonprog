class A:
    def __init__(self,a,b):
        self.valA = a
        self.valB = b

    def dispA(self):
        print("A = ",self.valA)
        print("B = ",self.valB)


class B(A):
    def __init__(self,a,b,c):
        #A.__init__(self,a,b)
        super().__init__(a,b)
        self.valc = c

    def dispB(self):
        print("A = ",self.valA)
        print("B = ",self.valB)
        print("C = ",self.valc)


ob1 = B(22,33,44)
ob1.dispB()



'''
ob = A(22,33)
ob.dispA()
'''
