#!/usr/bin/env python3
# Created By: Lennon Cehajic
# Date: October 22nd, 2026
# This program runs a random number guessing game.
import random


def main():
    # Get the guessed number from the user.
    user_guess = input(
        "Welcome to Lennon's random number guessing game. Guess a number between 0 and 9: "
    )

    # Generate the random number.
    random_variable = random.randint(1, 9)  # A number between 1 and 9

    # Try to cast to int, and check if the guessed number is equal to the correct number.
    try:
        user_guess_int = int(user_guess)

        if user_guess_int == random_variable:
            print("You have guessed correctly!")

        if user_guess_int != random_variable:
            print(
                "You have guessed incorrectly. The correct number was {}".format(
                    random_variable
                )
            )
    except:
        print("{} is not an integer. Please try again.".format(user_guess))

    finally:
        print("Thank you for playing.")


if __name__ == "__main__":
    main()
