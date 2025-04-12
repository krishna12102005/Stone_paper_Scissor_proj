import random

choices = ["Rock","Paper","Scissors"]
computer_guess = random.choice(choices)


while True:
    user_input = input("Rock, Paper or Scissors (r/p/s): ").lower()

    if user_input == "r":
        print("You chose Rock")
        print("Computer chose", computer_guess)

        if computer_guess == "Paper":
            print("You lose")
        elif computer_guess == "Scissors":
            print("You win")
        else:
            print("Both are the same")

    elif user_input == "p":  # <- Correct indentation here
        print("You chose Paper")
        print("Computer chose", computer_guess)

        if computer_guess == "Scissors":
            print("You lose")
        elif computer_guess == "Rock":
            print("You win")
        else:
            print("Both are the same")

    elif user_input == "s":
        print("You chose scissors")
        print("Computer chose", computer_guess)

        if computer_guess == "Rock":
            print("You lose ")
        elif computer_guess == "Paper":
            print("You win")
        else:
            print("Both are the same")

    else:
        print("Invalid Input!")
