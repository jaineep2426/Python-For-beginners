#Write a program to open three files 1.txt , 2.txt , 3.txt if any these files are not present , a message without exiting the program must be printed prompting the same

try:
    with open("prac60_1.txt" , "r") as f:
      print(f.read())
except Exception as e:
    print(e)

try:
    with open("prac60_2.txt" , "r") as f:
      print(f.read())
except Exception as e:
   print(e)

try:
   with open("prac60_3.txt" , "r") as f:
    print(f.read())
except Exception as e:
   print(e)

print("Thank You!!")   
