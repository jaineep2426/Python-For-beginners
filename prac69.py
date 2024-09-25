#Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce
l=[123 , 543 , 56 , 9876 , 45 , 4567890 , 98765 , 1234 ]


def greater(a , b):
    if (a>b):
         return a
    return b

print(reduce(greater , l))