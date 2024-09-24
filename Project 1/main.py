import random
'''
1 for snake
-1 for gun
0 for water'''

computer =random.choice([-1 , 0 , 1])
youstr = input("Enter Your Choice :")

youdisc={"s" : 1 , "g": -1 , "w" : 0 }
reversedisc={1 :"Snake" , -1 : "Gun" , 0 : "Water"}

you=youdisc[youstr]
print(f"You chose : {reversedisc[you]} \n Computer chose : {reversedisc[computer]}")

if(you == computer):
    print("With Draw")
else:
    if(computer == -1 and you== 0):
        print("You lose!")
    elif(computer== -1 and you==1):
        print("You win!")
    elif(computer== 1 and you==0):
        print("You lose!")
    elif(computer== 1 and you==-1):
        print("You win!")
    elif(computer== 0 and you==1):
        print("You win!")
    elif(computer== 0 and you==-1):
        print("You lose!")
    else:
        print("Something went wrong!")
