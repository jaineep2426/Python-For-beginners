class employee:
    def __init__(self):
        print("Constructor of employee")
    a=1

class manager(employee):
    def __init__(self):
        print("Constructor of manager")
    b=2

class customer(manager):
    def __init__(self):
        super().__init__()
        print("Constructor of customer")
    c=3

#o=employee()
#print(o.a)
#o=manager()
#print(o.a , o.b)
o=customer()
print(o.a , o.b , o.c)  