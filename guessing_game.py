import sys


class GuessingGame:
    def __init__(self):
        self._a = 0
        self._b = 100
        self.secret = -1
        self._guesses = 10  # Number of guesses remaining
        self.previous_guesses = []  # List to store previous guesses
        self.hasWon = False

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, minimum):
        try:
            assert minimum <= self._b
        except AssertionError:
            print("The minimum cannot be greater than the maximum")
        except AttributeError:
            pass
        else:
            self._a = minimum

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, maximum):
        try:
            assert maximum >= self._a
        except AssertionError:
            print("The maximum cannot be lesser than the minimum")
        except AttributeError:
            pass
        else:
            self._b = maximum

    @property
    def guesses(self):
        return self._guesses

    @guesses.setter
    def guesses(self, value):
        try:
            assert value > 0
        except AssertionError:
            print("Guesses must be > 0")
        else:
            self._guesses = value
