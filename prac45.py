#Write a program to find out whether a file is identical & matches the content of another file

with open("prac45_1.txt") as f:
    content1=f.read()

with open("prac45_2.txt")as f:
    content2=f.read()

if(content1 == content2):
    print("Both files are identical")
else:
    print("Both files are not identical")