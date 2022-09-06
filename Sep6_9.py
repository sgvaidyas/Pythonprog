try:
    fp = open("mydata1.txt","w")

    fp.write("i am writing line 1\n ")
    fp.write("i am writing line 2\n ")
    fp.write("i am writing line 3\n ")
    fp.write("i am writing line 4\n ")

    fp.close()
except:
    print("Error cannot create file ")
