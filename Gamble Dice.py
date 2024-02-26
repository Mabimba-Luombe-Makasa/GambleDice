import random

print("WELCOME TO GAMBLE DICE")
print("Get your card and casino games rolling with us...\n")

while True:
    try:
        user_selection = int(input("Press 1 to use a single dice.\nPress 2 for double dice.\nPress 0 to exit\n"))

        if user_selection == 1:
            game_dice_one = random.randint(1,6)

            print("The rolled dice result is: ", game_dice_one, "\n")

        elif user_selection == 2:
            game_dice_one = random.randint(1,6)
            game_dice_two = random.randint(1,6)

            print("The rolled dice result is: ", game_dice_one, "and: ", game_dice_two, "\n")

        elif user_selection == 0:
            print("Thank You for playing Gamble Dice. \n"
                  "Exiting....")

            break

        else:
            print("You have entered a wrong option. Press 1, 2 or 0\n")

    except ValueError:
        print("You have entered a wrong option. Try again using numerical characters.")
