class Product:
    def setProd(self):
        self.pid = int(input("Enter PID = "))
        self.pname = input("Enter the Pname = ")
        self.price = float(input("Enter the price = "))

    def disp(self):
        print("{}       | {}     | {}   ".format(self.pid,self.pname,self.price))

n = int(input("Enter the num of records = "))

recs = []

for i in range(n):
    ob = Product()
    ob.setProd()
    recs.append(ob)

print("PRODUCTS \n____________________")
for i in range(n):
    recs[i].disp()

recs = recs[::-1]

print("REVERSED PRODUCTS \n____________________")
for i in range(n):
    recs[i].disp()





