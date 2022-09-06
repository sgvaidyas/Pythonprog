try:
    s = input("Enter the string = ")
    ind = int(input("Enter the index = "))
    print("=========================")
    print("Char inside index = {} is {}".format(ind,s[ind]))
except IndexError:
    print("Index provided was out of range")
