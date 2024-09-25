#Write a program to input name , marks and phone number of a student and format it using the format function like below:
#"The name of the student is XYZ , his marks are 80 and phone number is 0987654321"

name = input("Enter name :")
marks = int(input("Enter marks:"))
phone= int(input("Phone no:"))

s ="The name of the student is {} , his marks are {} and phone number is {}".format(name , marks , phone)

print(s)