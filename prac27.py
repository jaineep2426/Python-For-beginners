#Calculate the factorial number of given number using loop

n=int(input("Enter the number :"))

product=1
for i in range(1,n+1):
    product=product*i
    print(f"The factorial of {n} is {product} ")