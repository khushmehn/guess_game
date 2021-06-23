import random


# MAIN -main()- FUNCTION FOR WHOLE GUESSING GAME.
# WHICH MAKES THE WHOLE CODE CONVENIENT AND EASE TO HANDLE FROM ANYWHERE YOU WANT TO.

def main():
    random_num = random.randint(1, 10)

    guess = None
    while guess != random_num:
        guess = int(input("Pick a number from 1 to 10: "))
        if guess > random_num:
            print("TOO HIGH!")
        elif guess < random_num:
            print("TOO LOW!")
        else:
            print("YOU WON")

            # RESTART FUNCTION -restart()- FOR GIVING THE APPROPRIATE OUTPUT BASED ON THE USER INPUT.
            def restart():
                play_again = input("Do you want to play again? (y/n) ")
                if play_again == "y":
                    main()
                elif play_again == "n":
                    print("Thank you for playing!:)")
                else:
                    print("Please enter a valid choice!")
                    restart()

            # INITIALIZING RESTART FUNCTION -restart()-
            restart()


# INITIALIZING MAIN FUNCTION -main()-
main()
