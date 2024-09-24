#Write a program to mine a log file and find out whether it contains "python"

with open("prac42.txt") as f:
    content=f.read()

if("Python" in content):
    print("Python is present")   
else:
    print("Python is not present") 