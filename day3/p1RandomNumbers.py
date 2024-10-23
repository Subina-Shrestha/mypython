import random
random_num=random.randint(1,4)
chance=0
while chance<3:
    if (chance==0):
        print("guess a number between 1 and 3")
    elif(chance>0):
        print("chance: ",chance+1)
    guess=int(input("enter your guess:"))
    if random_num==guess:
        print("congratulations! successful person you have entered the correct number")
        break
    elif random_num>guess:
        print("your guess is too low")
    else:
        print("your guess is too high")
    chance=chance+1
