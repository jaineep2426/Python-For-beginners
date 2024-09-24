#Write a program to make copy for "this.txt" file
with open("prac42.txt") as f:
    content=f.read()

with open("prac44.txt" ,"w") as f:
    f.write(content)