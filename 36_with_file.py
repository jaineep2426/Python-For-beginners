f=("33_file_write.txt")
print(f.read())
f.close()

#The same statement can be written using with statement like this

with open ("file.txt") as f:
    print(f.read())

#You do't have to explicitly close the file
