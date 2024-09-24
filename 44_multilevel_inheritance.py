class employee:
    a=1

class manager(employee):
    b=2

class customer(manager):
    c=3

o=employee()
print(o.a)
o=manager()
print(o.a , o.b)
o=customer()
print(o.a , o.b , o.c)    