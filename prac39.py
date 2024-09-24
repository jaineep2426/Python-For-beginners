#Write a program to generate multiple tables from 2 to 20 and write it to the different files. place this files in a folder for a 13 year old.

def generateTables(n):
    table=""
    for i in range(1 , 11):
        table+= f"{n} X {i} = {n*i}\n"

    with open(f"prac39_tables/table_{n}.txt" , "w") as f:  
        f.write(table)

for i in range(2 , 21):
    generateTables(i)           