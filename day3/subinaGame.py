import random
random_numb=random.randint(1,5)
chance=0
while(chance<4):
    if(chance==0):
        print("guess a number between 1 ans 5")
    user=int(input("guuess a number"))
    if (user==random_numb):
        print("congratulation!  saksessphool personnnnn")
        break
    elif(user>random_numb):
        print("sorry your guess is too high")
    else:
        print("your guess is too low")


