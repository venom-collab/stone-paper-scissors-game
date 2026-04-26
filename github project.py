import random

def play():
    choices = ["stone", "paper", "scissors"]

    user = input("Enter stone/paper/scissors: ")
    comp = random.choice(choices)

    print("Computer:", comp)

    if user == comp:
        print("Draw")
    elif user == "stone" and comp == "scissors":
        print("You Win")
    elif user == "paper" and comp == "stone":
        print("You Win")
    elif user == "scissors" and comp == "paper":
        print("You Win")
    else:
        print("You Lose")