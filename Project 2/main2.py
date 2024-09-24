#We are going to write a program that generates a random number and asks the user to guess it.

import random
n= random.randint(1 , 100)
a= -1
guesses=1
while(a !=n):
    guesses+=1
    a = int(input("Guess a number"))
    if(a>n):
        print("Lower number please")
        guesses+=1
    elif(a<n):
        print("Higher Number Please")
        guesses+=1

print(f"You have guess the number {n} correctly in {guesses} attempt")        