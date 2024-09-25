#Stores the multiplication tables generated in problem prac62 in a file named Tables.txt

n = int(input("Enter a number :"))

table =[n*i for i in range(1 , 11) ]
with open ("table64.txt" , "w") as f:
    f.write(str(table) + "\n")