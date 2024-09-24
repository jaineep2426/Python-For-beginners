a=int(input("Enter Your Age : "))

if(a%2 ==0):
    print("Your Age is Even")

if(a>=18):
    print("You are Eligible to Vote")
elif(a<0):
    print("Invalid Age")
elif(a==0):
    print("You are Entering in 0")
else:
    print("You are not Eligible to Vote")


print("End ")    