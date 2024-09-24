#Write a programm using functions to find greatest of three numbers

def greatest(a , b ,c):
    if(a>b and a>c):
        return a
    elif(b>c and b>a):
        return b
    else:
        return c
a=12
b=23
c=34

print(greatest(a , b , c))