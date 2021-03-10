"""
TODO: Convert to Modules
TODO: Add instructions
TODO: Implement Exception Handling
"""

from random import randint, sample, choice
from english_words import english_words_set as english
from guessing_game import *
from hangman import *
from datetime import datetime
from database import Database
import time



def main():
    global games, choices
    games = ["Guessing Game", "Hangman", "Cows and Bulls", "Reverse Guessing Game"]
    games.sort()

    games_list = games.copy()
    for i in range(len(games_list)):
        games_list[i] = games_list[i].lower()
        games_list[i] = games_list[i].replace(" ", "_")

    choices = dict(zip(range(1, len(games) + 1), games_list))


# A function that returns a user-inputted integer
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
    won = True
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
            won = False
            break
        time.sleep(1)
    if won:
        with Database("Guessing Game") as scores_db:
            scores_db.add_record(datetime.today().strftime('%d/%m/%Y'), name, gg.guesses, gg.b - gg.a + 1)
            scores_db.display()
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
    number = ''.join(["{}".format(randint(0, 9)) for num in range(0, digits)])
    print(number)
    while True:
        guess = input("Enter a guess\n> ")
        if guess == number:
            print("You win!")
            break
        bulls = 0
        cows = 0
        bulls_index = []

        # Find Bulls first
        for i in range(digits):
            if guess[i] == number[i]:
                bulls += 1
                bulls_index.append(i)

        # Find cows, ignoring bull indexes
        previous_cows = []
        for i in range(digits):
            if guess[i] in [j for p, j in enumerate(number) if p not in bulls_index] and guess[i] not in previous_cows:
                cows += 1
                previous_cows += guess[i]
        print("{} {}, {} {}".format(bulls, "bull" if bulls == 1 else "bulls", cows, "cow" if cows == 1 else "cows"))


def hangman():
    print("This is the Hangman game.")
    game = Hangman(sample(english, 1)[0])
    while not game.game_over():
        if game.guess(input("Enter a guess\n> ")):
            print("Good guess!")
        else:
            print("Bad guess.")
        game.display()
    print("You won!")


def main_menu():
    try:
        print("Please select one of the following {} options".format(len(games)))
        for index, game in enumerate(games, 1):
            print("\t{}. {}".format(index, game))
        print("\t{}. Exit".format(len(choices) + 1))
        selection = intput()
    except IndexError:
        print("Please select a number between 1 and", len(games) + 1)
    else:
        if selection == len(choices) + 1:
            print("Thanks for playing, goodbye!")
            exit(0)
        return eval(choices.get(selection))()


if __name__ == '__main__':
    main()
    print("Welcome to John's Mini Games!")
    global name
    name = input("What is your name?\n> ")
    print(f'Welcome, {name}!')
    time.sleep(1)
    main_menu()
