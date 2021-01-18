import sys


class GuessingGame:
    def __init__(self):
        self.a = 0
        self.b = 100
        self.secret = -1
        self.guesses = 10  # Number of guesses remaining
        self.previous_guesses = []  # List to store previous guesses
        self.hasWon = False

    # @property
    # def a(self):
    #     return self.a
    #
    # @a.setter
    # def a(self, minimum):
    #     try:
    #         assert minimum <= self.b
    #     except AssertionError:
    #         print("The minimum cannot be greater than the maximum")
    #     except AttributeError:
    #         pass
    #     else:
    #         self.a = minimum
    #
    # @property
    # def b(self):
    #     return self.b
    #
    # @b.setter
    # def b(self, maximum):
    #     try:
    #         assert maximum >= self.a
    #     except AssertionError:
    #         print("The maximum cannot be lesser than the minimum")
    #     except AttributeError:
    #         pass
    #     else:
    #         self.b = maximum
    #
    # @property
    # def guesses(self):
    #     return self.guesses
    #
    # @guesses.setter
    # def guesses(self, value):
    #     try:
    #         assert value > 0
    #     except AssertionError:
    #         print("Guesses must be > 0")
    #     else:
    #         self.guesses = value
