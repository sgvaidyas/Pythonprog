n = int(input("Enter the no of records = "))

try:
    fp = open("Myrec.txt","a")
    for i in range(n):
        try:
            name = input("Enter name = ")
            fp.write(name + "\n")
        except:
            print("Cannot insert data to file")
    fp.close()
except:
    print("Cannot create file")
        
