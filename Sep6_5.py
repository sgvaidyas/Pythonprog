try:
    s = input("Enter the string")
    print("S  = ",s)
    ch = int(input("Do you want to 1=>delete string 2=>no"))
    if ch==1:
        del s
    elif ch==2:
        pass
    else:
        print("Invalid choice")
    ind = int(input("Enter the index = "))
    print("Char at {} is {}".format(ind,s[ind]))
except ValueError:
    print("Datatype mismatch")
except NameError:
    print("Variable that u are trying to access does not exist/deleted")
except:
    print("Errors")
