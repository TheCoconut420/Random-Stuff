class Nim:
    def __init__(self):
        self._number_of_tries = 21
        self.user_starts = bool
        self.variable = str
    
    def take(self) -> int:
        self.varibale = int(input("Take at least one piece or a max of three pieces: "))
        if self.varibale == 1:
            self._number_of_tries -= 1
            print(f"You took one piece, there are now {self._number_of_tries} pieces left.")
        elif self.varibale == 2:
            self._number_of_tries -= 2
            print(f"You took two pieces, there are now {self._number_of_tries} pieces left.")
        elif self.varibale == 3:
            self._number_of_tries -= 3
            print(f"You took three pieces, there are now {self._number_of_tries} pieces left.")
        else:
            print("Invalid input, try again.")
            self.take(self)       

    def ai_turn(self) -> str:
        str(self.variable)
        if self.variable == 1:
            self._number_of_tries -= 3
            print(f"The AI took three piece, there are now {self._number_of_tries} pieces left.")
        elif self.variable == 2:
            self._number_of_tries -= 2
            print(f"The AI took two pieces, there are now {self._number_of_tries} pieces left.")
        elif self.variable == 3:
            self._number_of_tries -= 1
            print(f"The AI took one piece, there are now {self._number_of_tries} pieces left.")

    def is_finished(self) -> bool:
        if self._number_of_tries == 0:
            return True
        else:
            return False
    

    def is_won(self) -> bool:
        if self.is_finished() == True:

            print ("You won!")
        else:
            print ("You lost!")


game = Nim()

while True:
    game.variable = int(input("Choose: "))
    game.take()
    game.ai_turn()
    if game._number_of_tries == 0:    
        game.is_finished()
        game.is_won()
        break