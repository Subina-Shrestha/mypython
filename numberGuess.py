# Guess the Number(computer) 
import random

random_num = random.randint(0,9)
chance=0
    
while(chance<3):
    if(chance>0):
        print("Chance: ",(chance+1))
    user_input = int(input("Enter your guess: "))
    if(random_num == user_input):
        print("Your Guess is correct")
        break
    else:
        print("Your guess is incorrect")
    chance+=1


