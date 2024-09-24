#the game()function in the programm lets play a game and returns the score as an integer . You need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi-score.You need to write a program to update the Hi-score whenever the game() function break the High-score.

import random

def game():
    print("You are playing the game..")
    score=random.randint(1 , 56)
    #Fetch the highscore
    with open("prac38.txt") as f:
        highscore=f.read()
        if(highscore!=""):
            highscore = int(highscore)
        else:
            highscore = 0

    print(f"Your number is {score}")
    if(score>highscore):
        #write the highscore
        with open("prac38.txt", "w") as f:
            f.write(str(score))
    return score

game()
