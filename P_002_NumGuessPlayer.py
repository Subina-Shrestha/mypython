# P_002_NumGuessPlayer.py# Guess the Number (user) 
import random

print("Game rule:")
print("1.Two player can play this game.")
print("2.First player will choose the number")
print("3.Second player will guess the number")
print("4.Guess the number between 0~9")
print("5.You will have 3 chance")

chance = 0 # number of chances
users = [] # users names
chance_name = ["first","second","third"] # number of chances in word

#asking for names
for i in range(0,2):
    name = str(input("Enter the name of player "+str(i+1)+": ")) #asking value
    users.append(name) # adding value to the list

print(users[0] + " will choose the number") # print the name of player
random_num = int(input(users[0]+ ", enter the number:")) # choose the number
print("\nGame Starts Now:\n")
print(users[1] + " will guess the number") # declare player second will choose the number

#until chance is less than 3 and guess is correct, player can guess the number

while(chance!=3):
    guess = int(input("Enter the number:"))
    if(random_num == guess):
        print("Congratulations, You did it in",chance_name[chance],"try")
        break
    else:
        print("You didn't made it, Try again")
    chance+=1