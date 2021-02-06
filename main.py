"""
TODO: Convert to Modules
TODO: Add instrutions
TODO: Implement Hangman
TODO: Implement Cows and Bulls
"""

from random import randint, choice
from guessing_game import *
import time

games = ["Guessing Game", "Hangman", "Cows and Bulls", "Reverse Guessing Game"]
games.sort()

games_list = games.copy()
for i in range(len(games_list)):
    games_list[i] = games_list[i].lower()
    games_list[i] = games_list[i].replace(" ", "_")

choices = dict(zip(range(1, len(games) + 1), games_list))


def intput(prompt=""):
    try:
        symbol = "\n> " if prompt != "" else "> "
        user = int(input(prompt + symbol))
    except ValueError:
        print("Please enter an integer.")
    else:
        return user


def guessing_game():
    print("Welcome to the Guessing Game!")
    # TODO: Add instructions
    gg = GuessingGame()
    gg.a = intput("Please enter the minimum number")  # Lower bound, inclusive
    gg.b = intput("Please enter the maximum number")  # Upper bound, inclusive
    gg.secret = randint(gg.a, gg.b)  # A random number between a and b that is to be guessed
    gg.guesses = intput("Please enter the maximum number of guesses")  # Max number of tries to guess correctly

    while True:
        while True:
            try:
                guesses_str = "guess" if gg.guesses == 1 else "guesses"
                print("\n{} {} remaining!".format(gg.guesses, guesses_str))
                if gg.previous_guesses:
                    print("Previous Guesses: {}".format(gg.previous_guesses))
                guess = intput("Guess a number")
                assert gg.a <= guess <= gg.b
                if guess in gg.previous_guesses:
                    raise ValueError
            except TypeError:
                print("Please enter an integer.")
            except AssertionError:
                print("Please enter a number between {} and {}.".format(gg.a, gg.b))
            except ValueError:
                print("You have already guessed that! Please try another number.")
            else:
                gg.previous_guesses.append(guess)
                break

        if guess < gg.secret:
            print(guess, "is too low!")
        elif guess > gg.secret:
            print(guess, "is too high!")
        else:
            print("Congratulations, you guessed it!")
            break
        gg.previous_guesses.sort()
        gg.guesses -= 1
        if gg.guesses == 0:
            print("Sorry, you lost! The number was {}.".format(gg.secret))
            break
        time.sleep(1)
    if input("Would you like to play again?\n> ").lower() not in ("yes", "y"):
        print("Returning to the main menu.")
        main_menu()
    else:
        guessing_game()


def reverse_guessing_game():
    print("This is the reverse guessing game.")
    low = intput("Please enter the lower bound")
    high = intput("Please enter the upper bound")
    phrases = ["Is the number?", "Is it?", "Could it be?", "What is?", "It has to be!",
               "My guess is!", "I know it's!", "My senses tell me the number is.",
               "Roses are red,\nViolets are blue,\nThe number must be."]

    while True:
        guess = randint(low, high)
        phrase = choice(phrases)
        print("{} {}{}".format(phrase[:-1], guess, phrase[-1]))
        answer = intput("1. Higher\n2. Lower\n3. Correct")
        if (answer != 3 and high == low) or not (low < high):
            print("I have no idea then! You must've mislead me.")
            break
        elif answer == 1:
            low = guess + 1
        elif answer == 2:
            high = guess - 1
        else:
            print("Yay!")
            break


def cows_and_bulls():
    print("This is the Cows and Bulls game.")
    digits = intput("How many digits?")
    low = 10 ** (digits - 1)
    high = 10 ** digits - 1
    number = str(randint(low, high))
    print(low)
    print(high)
    print(number)

    while True:
        guess = input("Enter a guess\n> ")
        if guess == number:
            print("You win!")
            break
        bulls = 0
        cows = 0
        bulls_index = []

        for i in range(digits):
            if guess[i] == number[i]:
                bulls += 1
                bulls_index.append(guess[i])
            elif guess[i] in number:
                cows += 1
                    

        print("{} {}, {} {}".format(bulls, "bull" if bulls == 1 else "bulls", cows, "cow" if cows == 1 else "cows"))






def hangman():
    print("This is the Hangman game.")


def main_menu():
    try:
        print("Please select one of the following {} options".format(len(games)))
        for index, game in enumerate(games, 1):
            print("\t{}. {}".format(index, game))
        print("\t{}. Exit".format(len(choices) + 1))
        choice = intput()
    except IndexError:
        print("Please select a number between 1 and", len(games) + 1)
    else:
        if choice == len(choices) + 1:
            print("Thanks for playing, goodbye!")
            exit(0)
        return eval(choices.get(choice))()


if __name__ == '__main__':
    print("Welcome to John's Mini Games!")
    time.sleep(1)
    main_menu()
