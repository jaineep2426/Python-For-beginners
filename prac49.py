#Create a class with class attribute a , create an object from it and set 'a' directy using object.a=0 . does this change class attribute?

class Demo:
    a=4

o=Demo()
print(o.a)
o.a=1
print(o.a)
print(Demo.a)