marks1=int(input("Enter Your marks1 : "))
marks2=int(input("Enter Your marks2: "))
marks3=int(input("Enter Your marks3: "))

total_marks=(100)*(marks1+marks2+marks3)/300

if(total_marks>40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are pass",total_marks)
else:
    print("You are failed",total_marks)