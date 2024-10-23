# rock, paper, scissors

import random

while True: 
    user_input = input("Enter your choice(rock, paper, scissors): ")
    possible_action = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_action)
    print(f"You choose {user_input} and computer choose {computer_action}")


    if user_input == computer_action:
        print(f"Both choose same {user_input}, It's tie.")
    elif user_input == "rock":
        if computer_action == "scissors":
            print("Rock smashes Scissors. You win!!!")
        else:
            print("Paper covers rock. You Lose!!!")
    elif user_input == "scissors":
        if computer_action == "paper":
            print("Scissors cuts Paper. You win!!!")
        else:
            print("Rock smashes Scissors. You Lose")
    elif user_input == "paper":
        if computer_action == "rock":
            print("Paper covers Rock. You Win !!!")
        else:
            print("Scissors cuts Paper. You Lose!!!")
    
    play_again = input("Play Again (y/n)?")
    if play_again.lower() != "y":
        break