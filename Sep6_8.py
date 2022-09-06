try:
    fp = open("mydata1.txt","r")
    content = fp.read()
    print(content)
    fp.close()
except FileNotFoundError:
    print("File you are trying to read does not exist")
