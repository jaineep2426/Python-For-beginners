#Write a program to filter a list of numbers which are divisible by 5.

def divisible5(n):
    if(n%5==0):
        return True
    return False

a=[123 , 543 , 56 , 9876 , 45 , 4567890 , 98765 , 1234 ]

f=list(filter(divisible5 , a))
print(f)