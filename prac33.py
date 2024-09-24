#Functions to print first n lines of the following patterns
'''
***
**
*
'''

def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)

pattern(5)