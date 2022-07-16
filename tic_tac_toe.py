play_field = [" "] * 9
player_1 = "X"
player_2 = "O"

class tic_tac_toe:
    def __init__(self):
        self.play_field = [" "] * 9
        self.player_1 = "X"
        self.player_2 = "O"
        self.player_1_win = False
        self.player_2_win = False
        self.draw = False
    
    def show_field(self):
        print(self.play_field[0:3])
        print(self.play_field[3:6])
        print(self.play_field[6:9])
    
    def player_1_turn(self):
        player_1_try = int(input("Player 1, choose a number: "))
        if player_1_try < 1 or player_1_try > 9:
            print("The number can't be lower than 1 or higher than 9")
            self.player_1_turn()
        elif self.play_field[player_1_try - 1] == "X" or self.play_field[player_1_try - 1] == "O":
            print("This number is already taken")
            self.player_1_turn()
        else:
            self.play_field[player_1_try - 1] = "X"
        self.check_draw()
        self.check_win()
    
    def player_2_turn(self):
        player_2_try = int(input("Player 2, choose a number: "))
        if player_2_try < 1 or player_2_try > 9:
            print("The number can't be lower than 1 or higher than 9")
            self.player_2_turn()
        elif self.play_field[player_2_try - 1] == "X" or self.play_field[player_2_try - 1] == "O":
            print("This number is already taken")
            self.player_2_turn()
        else:
            self.play_field[player_2_try - 1] = "O"
        self.check_draw()
        self.check_win()

    def check_win(self):
        if self.play_field[0] == self.play_field[1] == self.play_field[2] == "X":
            self.player_1_win = True
        elif self.play_field[0] == self.play_field[1] == self.play_field[2] == "O":
            self.player_2_win = True
        elif self.play_field[3] == self.play_field[4] == self.play_field[5] == "X":
            self.player_1_win = True
        elif self.play_field[3] == self.play_field[4] == self.play_field[5] == "O":
            self.player_2_win = True
        elif self.play_field[6] == self.play_field[7] == self.play_field[8] == "X":
            self.player_1_win = True
        elif self.play_field[6] == self.play_field[7] == self.play_field[8] == "O":
            self.player_2_win = True
        elif self.play_field[0] == self.play_field[3] == self.play_field[6] == "X":
            self.player_1_win = True
        elif self.play_field[0] == self.play_field[3] == self.play_field[6] == "O":
            self.player_2_win = True
        elif self.play_field[1] == self.play_field[4] == self.play_field[7] == "X":
            self.player_1_win = True
        elif self.play_field[1] == self.play_field[4] == self.play_field[7] == "O":
            self.player_2_win = True
        elif self.play_field[2] == self.play_field[5] == self.play_field[8] == "X":
            self.player_1_win = True
        elif self.play_field[2] == self.play_field[5] == self.play_field[8] == "O":
            self.player_2_win = True
        elif self.play_field[0] == self.play_field[4] == self.play_field[8] == "X":
            self.player_1_win = True
        elif self.play_field[0] == self.play_field[4] == self.play_field[8] == "O":
            self.player_2_win = True
        elif self.play_field[2] == self.play_field[4] == self.play_field[6] == "X":
            self.player_1_win = True
        elif self.play_field[2] == self.play_field[4] == self.play_field[6] == "O":
            self.player_2_win = True
        else:
            return
    
    def check_draw(self):
        if " " in self.play_field:
            self.draw = False
        else:
            self.draw = True
    
    def play(self):
        self.show_field()
        self.player_1_turn()
        if self.player_1_win == True:
            print("\n")
            print("Player 1 wins")
            return
        if self.check_draw == True:
            print("\n")
            print("Draw")
            return
        self.show_field()
        self.player_2_turn()
        if self.player_2_win == True:
            print("\n")
            print("Player 2 wins")
            return
        if self.check_draw == True:
            print("\n")
            print("Draw")
            return
        self.play()
        
        
ttt = tic_tac_toe()
ttt.play()