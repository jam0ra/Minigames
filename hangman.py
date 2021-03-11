class Hangman:
    def __init__(self, word, lives=10):
        self.word = word
        self.lives = lives
        self.guesses = []
        self.masked = ['_'] * len(word)
        self.output = " ".join(self.masked)

    def display(self):
        self.output = " ".join(self.masked)
        print(self.output)
        print("{} lives remaining.".format(self.lives))

    def guess(self, letter):
        if letter not in self.guesses:
            self.guesses.append(letter)

        if letter not in self.word:
            self.lives -= 1
            return False
        else:
            for i, character in enumerate(self.word):
                if character == letter:
                    self.masked[i] = letter
        self.output = " ".join(self.masked)
        return True

    def game_over(self):
        if self.output.replace(" ", "") == self.word or self.lives == 0:
            return True
        return False
