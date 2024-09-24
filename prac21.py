marks=int(input("Enter Your Marks :"))

if(marks<100 and marks>90):
    print("Your are Excellent!")
elif(marks>80 and marks<90):
        print("Your grade is A")
elif(marks>70 and marks<80):
      print("Your grade is B")
elif(marks>60 and marks<70):
      print("Your grade is C")
elif(marks>50 and marks<60):
      print("Your grade is D")
else:
      print("Your grade is F")