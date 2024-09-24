#Write a program to find out the line number whether Python is present from prac42


with open("prac42.txt") as f:
    lines=f.readlines()
lineno=1 
for line in lines:
        if("Python" in line):
            print(f"Python is present in lineNo.{lineno}")   
            break
            lineno+=1
else:
    print("Python is not present") 