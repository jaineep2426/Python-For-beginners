a = int(input("Enter first number"))
b = int(input("Enter second number"))

if(b == 0):
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
else:
    print(f"Division of a/b is {a/b}")