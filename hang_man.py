import random


class Hangman:
    def __init__(self):
        self.word_list = ["able", "about", "account", "acid"]
        self.word = ""
        self.hidden_word = ""
        self.player_list = []
        self.player = 1
        self.max_player = 0
        self.lives = 10
        self.won = False

    def define_word(self):
        print("\n")
        choose = int(input("Do you want to decide the word or get a random word? (1 = choose self, 2 = random word): "))
        if choose == 1:
            self.word = str.lower(input("Enter the word: "))
            self.word = self.word.replace(" ", "-")
            self.word = list(self.word)
            self.hidden_word = [""] * len(self.word)
            for i in range(len(self.word)):
                if self.word[i] == "-":
                    self.hidden_word[i] = "-"
                
        elif choose == 2:
            self.word = list(self.word_list[random.randint(0, len(self.word_list) - 1)])
            self.hidden_word = [""] * len(self.word)

    def check_alive(self):
        if self.lives == 0:
            print("You are dead!")
            return False

    def get_word(self):
        print(self.hidden_word)

    def get_player(self):
        self.player_count = int(input("Enter the number of players: "))
        self.max_player = self.player_count
        for i in range(self.player_count):
            self.player_list.append(input("Enter the name of player " + str(i + 1) + ": "))

    def next_player(self):
        if self.player == self.max_player:
            self.player = 1
        else:
            self.player += 1
    
    def check_win(self):
        if self.hidden_word == self.word:
            print(f"{self.player_list[self.player - 1]} guessed the word!")
            self.won = True

    def guess(self):
        print("\n")
        self.get_word()
        guess = input(f"{self.player_list[self.player - 1]} Enter your guess: ")
        if guess in self.word:
            for j in range(len(self.word)):
                if guess == self.word[j]:
                    self.hidden_word[j] = guess
            print("Correct guess")
        else:
            print("Wrong guess!")
            self.lives -= 1
            print(f"You have {self.lives} lives left")
        self.check_win()
        if self.won == False:
            self.next_player()
            self.guess()

hang = Hangman()
hang.define_word()
hang.get_player()
hang.guess()