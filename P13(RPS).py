import random
while (True):
    user_choice=input("Enter: Rock, Paper or Scissors")
    options=["rock","paper","scissors"]
    opponent=random.choice(options)
    print(opponent)
    if user_choice not in ("rock","paper","scissors"):
        print("Invalid Input")
        continue
    if user_choice=="rock":
        if opponent=="paper":
            print("The computer chose paper, you lost")
        elif opponent=="scissors":
            print("The computer chose scissors, you won")
        else:
            print("The computer chose rock, it's a draw")
    elif user_choice=="paper":
        if opponent=="scissors":
            print("The computer chose scissors, you lost")
        elif opponent=="rock":
            print("The computer chose rock, you won")
        else:
            print("The computer chose paper, it's a draw")
    elif user_choice=="scissors":
        if opponent=="rock":
            print("The computer chose rock, you lost")
        elif opponent=="paper":
            print("The computer chose paper, you won")
        else:
            print("The computer chose scissors, it's a draw")
    else:
        print("Invalid Input")