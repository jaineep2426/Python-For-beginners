#A file contains a word "donkey" multiple times.You need to write a program which replace this word with ##### by updating the same file.

word = "Donkey"

with open("prac40.txt" , "r") as f:
    content=f.read()
newcontent=content.replace(word , "######")

with open("prac40.txt" , "w") as f:
    f.write(newcontent)    