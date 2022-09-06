#exception handling
try:
    num1 = int(input("Enter a numerator = "))
    num2 = int(input("Enter a denominator = "))
    res = num1/num2
    print("Result = ",res)
except ZeroDivisionError:
    print("Error: denominator should not be zero ")
except:
    print("Generic Error")
print(" hi this is just a sample line")
print("Second sample line")

