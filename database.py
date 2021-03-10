import sqlite3

guessing_game = '''
        CREATE TABLE IF NOT EXISTS guessing_game
            (date TEXT, name TEXT, attempts INTEGER, range INTEGER)
        '''

hangman = '''
        CREATE TABLE IF NOT EXISTS hangman
            (date TEXT, name TEXT, attempts INTEGER, word TEXT)
        '''

cows_and_bulls = '''
        CREATE TABLE IF NOT EXISTS cows_and_bulls
            (date TEXT, name TEXT, attempts INTEGER, digits INTEGER)
        '''

class Database:
    def __init__(self, game):
        self.connection = sqlite3.connect("scores.db")
        self.cursor = self.connection.cursor()
        if game == "Guessing Game":
            game = guessing_game
            self.name = "guessing_game"
        elif game == "Hangman":
            game = hangman
            self.name = "hangman"
        elif game == "Cows and Bulls":
            game = cows_and_bulls
            self.name = "cows_and_bulls"
        self.cursor.execute(game)

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        self.cursor.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()

    def display(self, order="date"):
        self.cursor.execute(f"SELECT rowid, * FROM {self.name} ORDER BY {order} DESC")
        for row in self.cursor.fetchall():
            print(row)

    def display_values(self, order="date", values=10):
        self.cursor.execute(f"SELECT rowid, * FROM {self.name} ORDER BY {order} DESC")
        for row in self.cursor.fetchmany(values):
            print(row)

    def add_record(self, date, player, attempts, value):
        self.cursor.execute(f"INSERT INTO {self.name} VALUES (?, ?, ?, ?)", (date, player, attempts, str(value)))

    
