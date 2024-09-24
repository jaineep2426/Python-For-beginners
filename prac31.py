#Using function to convert celcious to fahernheit

def f_to_c(f):
    return 5*(f-32)/9
f=int(input("Enter the Number F :"))
c=f_to_c(f)
print(round(c ,2 ))