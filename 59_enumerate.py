l =[23 , 67, 90 , 1]

index = 0
for item in l:
    print(f"The item number at index {index} is {item}")
    index+=1

#This can be simplied using enumerate function

for index , item in enumerate(l):
    print(f"The item number at index {index} is {item}")