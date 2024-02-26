# Imports random that can do random functions
import random

# Title and tag line
print("WELCOME TO GAMBLE DICE")
print("Get your card and casino games rolling with us...\n")

# While loop is to keep the app running
while True:
    # Checks is user has entered a numerical character
    try:
        # User input option
        user_selection = int(input("Press 1 to use a single dice.\nPress 2 for double dice.\nPress 0 to exit\n"))

        # If user enters option 1 it generates a random number from 1 to 6 and gives out the result
        if user_selection == 1:
            game_dice_one = random.randint(1,6)

            print("The rolled dice result is: ", game_dice_one, "\n")

        # If user enters option 2 it generates two different random numbers from 1 to 6 and gives out result
        elif user_selection == 2:
            game_dice_one = random.randint(1,6)
            game_dice_two = random.randint(1,6)

            print("The rolled dice result is: ", game_dice_one, "and: ", game_dice_two, "\n")

        # If user selects option 0 the app stops running
        elif user_selection == 0:
            print("Thank You for playing Gamble Dice. \n"
                  "Exiting....")

            break

        # Error handling if the user enters the wrong option
        else:
            print("You have entered a wrong option. Press 1, 2 or 0\n")

    # Error handling if user doesn't enter a numerical character
    except ValueError:
        print("You have entered a wrong option. Try again using numerical characters.")
