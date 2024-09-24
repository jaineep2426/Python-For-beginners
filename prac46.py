#Write a program to wipe out the comtent of a file

with open("prac44.txt" , "t+r")as f:
    f.truncate()