class Product:
    def __init__(self):
        self.pid = 0
        self.pname = ""
        self.price = 0

    def setdata(self):
        self.pid = int(input("Enter the pid  =  "))
        self.pname = input("Enter the pname = ")
        self.price = float(input("Enter the price  = "))

    def display(self):
        print("--------------------------")
        print("PId             = ",self.pid)
        print("PNAME           = ",self.pname)
        print("PRICE           = ",self.price)

#main
master = []
while(True):
    print("1 Insert 2 DISPLAY  3 SEARCH 4 EXIT")
    ch = int(input("Enter the choice = "))
    if ch ==1 :
        ob = Product()
        ob.setdata()
        master.append(ob)

    elif ch==2:
        print("RECORDS = ")
        for x in master:
            x.display()

    elif ch==3:
        pid = int(input("Enter the id  = "))
        isFound = False

        for x in master:
            if pid == x.pid:
                print("RECORD FOUND")
                print("---------------")
                x.display()
                isFound = True
                break
        if isFound == False:
            print("RECORD NOT FOUND ")

    elif ch==4:
        break

    else:
        print("Invalid choice ")





