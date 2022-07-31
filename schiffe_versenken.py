class ShipDestroyer:
    def __init__(self):
        self.wave = " "
        self.play_field_1  = [self.wave] * 100
        self.play_field_2 = [self.wave] * 100 
        self.ship_field_1  = [self.wave] * 100 
        self.ship_field_2 = [self.wave] * 100
        self.player_count = 2
        self.player = 1
        self.ship_length = 4
        self.player_1_win = False
        self.player_2_win = False

    def get_play_field(self):
        print("\n")
        print("    1    2    3    4    5    6    7    8    9    10")
        if self.player == 1:
            print("A", self.play_field_1[0:10])
            print("B", self.play_field_1[10:20])
            print("C", self.play_field_1[20:30])
            print("D", self.play_field_1[30:40])
            print("E", self.play_field_1[40:50])
            print("F", self.play_field_1[50:60])
            print("G", self.play_field_1[60:70])
            print("H", self.play_field_1[70:80])
            print("I", self.play_field_1[80:90])
            print("J", self.play_field_1[90:100])
        else:
            print("A", self.play_field_2[0:10])
            print("B", self.play_field_2[10:20])
            print("C", self.play_field_2[20:30])
            print("D", self.play_field_2[30:40])
            print("E", self.play_field_2[40:50])
            print("F", self.play_field_2[50:60])
            print("G", self.play_field_2[60:70])
            print("H", self.play_field_2[70:80])
            print("I", self.play_field_2[80:90])
            print("J", self.play_field_2[90:100])

    def get_ship_field(self):
        print("\n")
        print("    1    2    3    4    5    6    7    8    9    10")
        if self.player == 1:
            print("A",  self.ship_field_1[0:10])
            print("B", self.ship_field_1[10:20])
            print("C", self.ship_field_1[20:30])
            print("D", self.ship_field_1[30:40])
            print("E", self.ship_field_1[40:50])
            print("F", self.ship_field_1[50:60])
            print("G", self.ship_field_1[60:70])
            print("H", self.ship_field_1[70:80])
            print("I", self.ship_field_1[80:90])
            print("J", self.ship_field_1[90:100])
        else:
            print("A", self.ship_field_2[0:10])
            print("B", self.ship_field_2[10:20])
            print("C", self.ship_field_2[20:30])
            print("D", self.ship_field_2[30:40])
            print("E", self.ship_field_2[40:50])
            print("F", self.ship_field_2[50:60])
            print("G", self.ship_field_2[60:70])
            print("H", self.ship_field_2[70:80])
            print("I", self.ship_field_2[80:90])
            print("J", self.ship_field_2[90:100])

    def get_shot_letter(self):
        self.shot_letter = input("Letter: ")
        self.shot_letter = self.shot_letter.upper()
        if self.shot_letter == "A":
            self.shot_letter = 0
        elif self.shot_letter == "B":
            self.shot_letter = 10
        elif self.shot_letter == "C":
            self.shot_letter = 20
        elif self.shot_letter == "D":
            self.shot_letter = 30
        elif self.shot_letter == "E":
            self.shot_letter = 40
        elif self.shot_letter == "F":
            self.shot_letter = 50
        elif self.shot_letter == "G":
            self.shot_letter = 60
        elif self.shot_letter == "H":
            self.shot_letter = 70
        elif self.shot_letter == "I":
            self.shot_letter = 80
        elif self.shot_letter == "J":
            self.shot_letter = 90
        else:
            print("You entered an invalid letter!")
            self.get_shot_letter()
        if self.rotate == "y":
            if (self.shot_letter / 10) + self.ship_length > 10:
                print("You entered an illegal input!")
                self.get_shot_letter()
        
    def get_shot_number(self):
        if self.rotate != "y":
            self.shot_number = int(input("Number: "))
            if self.shot_number < 1 or self.shot_number > 10 or self.shot_number + self.ship_length > 11:
                print("You entered an illegal input!")
                self.get_shot_number()
        else:
            self.shot_number = int(input("Number: "))
            if self.shot_number < 1 or self.shot_number > 10:
                print("You entered an illegal input!")
                self.get_shot_number()

    def get_rotate(self):
        self.rotate = input("Rotate? (y/n): ")
        self.rotate = self.rotate.lower()
        if self.rotate != "y" and self.rotate != "n":
            print("You entered an illegal input!")
            self.get_rotate()

    def check_placement(self):
        if self.player == 1:
            if self.rotate == "n":
                for i in range(self.ship_length):
                    if self.ship_field_1[self.shot_number - 1 + i + self.shot_letter] == "o" or self.ship_field_1[self.shot_number - 1 + i + self.shot_letter] == "X":
                        self.invalid_input()
            else:
                for i in range(self.ship_length):
                    if self.play_field_1[self.shot_number - 1 + (i*10) + self.shot_letter] == "o" or self.ship_field_1[self.shot_number - 1 + (i*10) + self.shot_letter] == "X":
                        self.invalid_input()
        else:
            if self.rotate == "n":
                for i in range(self.ship_length):
                    if self.ship_field_2[self.shot_number - 1 + i + self.shot_letter] == "o" or self.play_field_2[self.shot_number - 1 + i + self.shot_letter] == "X":
                        self.invalid_input()
            else:
                for i in range(self.ship_length):
                    if self.play_field_2[self.shot_number - 1 + (i*10) + self.shot_letter] == "o" or self.ship_field_2[self.shot_number - 1 + (i*10) + self.shot_letter] == "X":
                        self.invalid_input()

    def invalid_input(self):
        print("You entered an illegal input!")
        self.get_ship_field()
        self.get_rotate()
        self.get_shot_letter()
        self.get_shot_number()
        self.check_placement()

    def place_ship(self):
        self.get_rotate()
        self.get_shot_letter()
        self.get_shot_number()
        self.check_placement()
        if self.player == 1:
            for i in range(self.ship_length):
                if self.rotate == "n":
                    self.ship_field_1[self.shot_number - 1 + i + self.shot_letter] = "X"
                    if self.shot_number != 1 and self.shot_number + self.ship_length != 11 and self.shot_letter != 0 and self.shot_letter != 90:
                        self.ship_field_1[(self.shot_number - 1 + i + self.shot_letter) - 10] = "o"
                        self.ship_field_1[(self.shot_number - 1 + i + self.shot_letter) + 10] = "o"
                        self.ship_field_1[(self.shot_number - 1 - 1 + self.shot_letter)] = "o"
                        self.ship_field_1[(self.shot_number - 1 + self.shot_letter + self.ship_length)] = "o"
                    elif self.shot_number == 1 and self.shot_letter == 0:
                        self.ship_field_1[(self.shot_number - 1 + i + self.shot_letter) + 10] = "o"
                        self.ship_field_1[(self.shot_number - 1 + self.shot_letter + self.ship_length)] = "o"
                    elif self.shot_number != 1 and self.shot_number + self.ship_length != 11 and self.shot_letter == 0:
                        self.ship_field_1[(self.shot_number - 1 + i + self.shot_letter) + 10] = "o"
                        self.ship_field_1[(self.shot_number - 1 - 1 + self.shot_letter)] = "o"
                        self.ship_field_1[(self.shot_number - 1 + self.shot_letter + self.ship_length)] = "o"
                    elif self.shot_number + self.ship_length == 11 and self.shot_letter == 0:
                        self.ship_field_1[(self.shot_number - 1 + i + self.shot_letter) + 10] = "o"
                        self.ship_field_1[(self.shot_number - 1 - 1 + self.shot_letter)] = "o"
                    elif self.shot_number == 1 and self.shot_letter == 90:
                        self.ship_field_1[(self.shot_number - 1 + i + self.shot_letter) - 10] = "o"
                        self.ship_field_1[(self.shot_number - 1 + self.shot_letter + self.ship_length)] = "o"
                    elif self.shot_number != 1 and self.shot_number + self.ship_length != 11 and self.shot_letter == 90:
                        self.ship_field_1[(self.shot_number - 1 + i + self.shot_letter) - 10] = "o"
                        self.ship_field_1[(self.shot_number - 1 - 1 + self.shot_letter)] = "o"
                        self.ship_field_1[(self.shot_number - 1 + self.shot_letter + self.ship_length)] = "o"
                    elif self.shot_number + self.ship_length == 11 and self.shot_letter == 90:
                        self.ship_field_1[(self.shot_number - 1 + i + self.shot_letter) - 10] = "o"
                        self.ship_field_1[(self.shot_number - 1 - 1 + self.shot_letter)] = "o"
                    elif self.shot_number == 1 and self.shot_letter != 0 and self.shot_letter != 90:
                        self.ship_field_1[(self.shot_number - 1 + i + self.shot_letter) + 10] = "o"
                        self.ship_field_1[(self.shot_number - 1 + i + self.shot_letter) - 10] = "o"
                        self.ship_field_1[(self.shot_number - 1 + self.shot_letter + self.ship_length)] = "o"
                    elif self.shot_number + self.ship_length == 11 and self.shot_letter != 0 and self.shot_letter != 90:
                        self.ship_field_1[(self.shot_number - 1 + i + self.shot_letter) - 10] = "o"
                        self.ship_field_1[(self.shot_number - 1 + i + self.shot_letter) + 10] = "o"
                        self.ship_field_1[(self.shot_number - 1 - 1 + self.shot_letter)] = "o"
                else:
                    self.ship_field_1[self.shot_number - 1 + (i*10) + self.shot_letter] = "X"
                    if self.shot_number != 1 and self.shot_number != 10 and self.shot_letter != 0 and (self.shot_letter / 10) + self.ship_length != 10:
                        self.ship_field_1[(self.shot_number - 1 + (i*10) + self.shot_letter) - 1] = "o"
                        self.ship_field_1[(self.shot_number - 1 + (i*10) + self.shot_letter) + 1] = "o"
                        self.ship_field_1[(self.shot_number - 1 - 10 + self.shot_letter)] = "o"
                        self.ship_field_1[(self.shot_number - 1 + (10 * self.ship_length) + self.shot_letter)] = "o"
                    elif self.shot_number == 1 and self.shot_letter == 0:
                        self.ship_field_1[(self.shot_number - 1 + (i*10) + self.shot_letter) + 1] = "o"
                        self.ship_field_1[(self.shot_number - 1 + (10 * self.ship_length) + self.shot_letter)] = "o"
                    elif self.shot_number != 1 and self.shot_number != 10 and self.shot_letter == 0:
                        self.ship_field_1[(self.shot_number - 1 + (i*10) + self.shot_letter) + 1] = "o"
                        self.ship_field_1[(self.shot_number - 1 + (i*10) + self.shot_letter) + -1] = "o"
                        self.ship_field_1[(self.shot_number - 1 + (10 * self.ship_length) + self.shot_letter)] = "o"
                    elif self.shot_number == 10 and self.shot_letter == 0:
                        self.ship_field_1[(self.shot_number - 1 + (i*10) + self.shot_letter) + -1] = "o"
                        self.ship_field_1[(self.shot_number - 1 + (10 * self.ship_length) + self.shot_letter)] = "o"
                    elif self.shot_number == 1 and (self.shot_letter / 10) + self.ship_length == 10:
                        self.ship_field_1[(self.shot_number - 1 + (i*10) + self.shot_letter) + 1] = "o"
                        self.ship_field_1[(self.shot_number - 1 - 10 + self.shot_letter)] = "o"
                    elif self.shot_number != 1 and self.shot_number != 10 and (self.shot_letter / 10) + self.ship_length == 10:
                        self.ship_field_1[(self.shot_number - 1 + (i*10) + self.shot_letter) - 1] = "o"
                        self.ship_field_1[(self.shot_number - 1 + (i*10) + self.shot_letter) + 1] = "o"
                        self.ship_field_1[(self.shot_number - 1 - 10 + self.shot_letter)] = "o"
                    elif self.shot_number == 10 and (self.shot_letter / 10) + self.ship_length == 10:
                        self.ship_field_1[(self.shot_number - 1 + (i*10) + self.shot_letter) - 1] = "o"
                        self.ship_field_1[(self.shot_number - 1 - 10 + self.shot_letter)] = "o"
                    elif self.shot_number != 1 and self.shot_number != 10 and self.shot_letter and self.shot_letter == 0:
                        self.ship_field_1[(self.shot_number - 1 + (i*10) + self.shot_letter) - 1] = "o"
                        self.ship_field_1[(self.shot_number - 1 + (i*10) + self.shot_letter) + 1] = "o"
                        self.ship_field_1[(self.shot_number - 1 + (10 * self.ship_length) + self.shot_letter)] = "o"
                    elif self.shot_number == 1 and self.shot_letter != 0 and (self.shot_letter / 10) + self.ship_length != 10:
                        self.ship_field_1[(self.shot_number - 1 + (i*10) + self.shot_letter) + 1] = "o"
                        self.ship_field_1[(self.shot_number - 1 - 10 + self.shot_letter)] = "o"
                        self.ship_field_1[(self.shot_number - 1 + (10 * self.ship_length) + self.shot_letter)] = "o"
                    elif self.shot_number == 10 and self.shot_letter != 0 and (self.shot_letter / 10) + self.ship_length != 10:
                        self.ship_field_1[(self.shot_number - 1 + (i*10) + self.shot_letter) - 1] = "o"
                        self.ship_field_1[(self.shot_number - 1 - 10 + self.shot_letter)] = "o"
                        self.ship_field_1[(self.shot_number - 1 + (10 * self.ship_length) + self.shot_letter)] = "o"
        else:
            for i in range(self.ship_length):
                if self.rotate == "n":
                    self.ship_field_2[self.shot_number - 1 + i + self.shot_letter] = "X"
                    if self.shot_number != 1 and self.shot_number + self.ship_length != 11 and self.shot_letter != 0 and self.shot_letter != 90:
                        self.ship_field_2[(self.shot_number - 1 + i + self.shot_letter) - 10] = "o"
                        self.ship_field_2[(self.shot_number - 1 + i + self.shot_letter) + 10] = "o"
                        self.ship_field_2[(self.shot_number - 1 - 1 + self.shot_letter)] = "o"
                        self.ship_field_2[(self.shot_number - 1 + self.shot_letter + self.ship_length)] = "o"
                    elif self.shot_number == 1 and self.shot_letter == 0:
                        self.ship_field_2[(self.shot_number - 1 + i + self.shot_letter) + 10] = "o"
                        self.ship_field_2[(self.shot_number - 1 + self.shot_letter + self.ship_length)] = "o"
                    elif self.shot_number != 1 and self.shot_number + self.ship_length != 11 and self.shot_letter == 0:
                        self.ship_field_2[(self.shot_number - 1 + i + self.shot_letter) + 10] = "o"
                        self.ship_field_2[(self.shot_number - 1 - 1 + self.shot_letter)] = "o"
                        self.ship_field_2[(self.shot_number - 1 + self.shot_letter + self.ship_length)] = "o"
                    elif self.shot_number + self.ship_length == 11 and self.shot_letter == 0:
                        self.ship_field_2[(self.shot_number - 1 + i + self.shot_letter) + 10] = "o"
                        self.ship_field_2[(self.shot_number - 1 - 1 + self.shot_letter)] = "o"
                    elif self.shot_number == 1 and self.shot_letter == 90:
                        self.ship_field_2[(self.shot_number - 1 + i + self.shot_letter) - 10] = "o"
                        self.ship_field_2[(self.shot_number - 1 + self.shot_letter + self.ship_length)] = "o"
                    elif self.shot_number != 1 and self.shot_number + self.ship_length != 11 and self.shot_letter == 90:
                        self.ship_field_2[(self.shot_number - 1 + i + self.shot_letter) - 10] = "o"
                        self.ship_field_2[(self.shot_number - 1 - 1 + self.shot_letter)] = "o"
                        self.ship_field_2[(self.shot_number - 1 + self.shot_letter + self.ship_length)] = "o"
                    elif self.shot_number + self.ship_length == 11 and self.shot_letter == 90:
                        self.ship_field_2[(self.shot_number - 1 + i + self.shot_letter) - 10] = "o"
                        self.ship_field_2[(self.shot_number - 1 - 1 + self.shot_letter)] = "o"
                    elif self.shot_number == 1 and self.shot_letter != 0 and self.shot_letter != 90:
                        self.ship_field_2[(self.shot_number - 1 + i + self.shot_letter) + 10] = "o"
                        self.ship_field_2[(self.shot_number - 1 + i + self.shot_letter) - 10] = "o"
                        self.ship_field_2[(self.shot_number - 1 + self.shot_letter + self.ship_length)] = "o"
                    elif self.shot_number + self.ship_length == 11 and self.shot_letter != 0 and self.shot_letter != 90:
                        self.ship_field_2[(self.shot_number - 1 + i + self.shot_letter) - 10] = "o"
                        self.ship_field_2[(self.shot_number - 1 + i + self.shot_letter) + 10] = "o"
                        self.ship_field_2[(self.shot_number - 1 - 1 + self.shot_letter)] = "o"
                else:
                    self.ship_field_2[self.shot_number - 1 + (i*10) + self.shot_letter] = "X"
                    if self.shot_number != 1 and self.shot_number != 10 and self.shot_letter != 0 and (self.shot_letter / 10) + self.ship_length != 10:
                        self.ship_field_2[(self.shot_number - 1 + (i*10) + self.shot_letter) - 1] = "o"
                        self.ship_field_2[(self.shot_number - 1 + (i*10) + self.shot_letter) + 1] = "o"
                        self.ship_field_2[(self.shot_number - 1 - 10 + self.shot_letter)] = "o"
                        self.ship_field_2[(self.shot_number - 1 + (10 * self.ship_length) + self.shot_letter)] = "o"
                    elif self.shot_number == 1 and self.shot_letter == 0:
                        self.ship_field_2[(self.shot_number - 1 + (i*10) + self.shot_letter) + 1] = "o"
                        self.ship_field_2[(self.shot_number - 1 + (10 * self.ship_length) + self.shot_letter)] = "o"
                    elif self.shot_number != 1 and self.shot_number != 10 and self.shot_letter == 0:
                        self.ship_field_2[(self.shot_number - 1 + (i*10) + self.shot_letter) + 1] = "o"
                        self.ship_field_2[(self.shot_number - 1 + (i*10) + self.shot_letter) + -1] = "o"
                        self.ship_field_2[(self.shot_number - 1 + (10 * self.ship_length) + self.shot_letter)] = "o"
                    elif self.shot_number == 10 and self.shot_letter == 0:
                        self.ship_field_2[(self.shot_number - 1 + (i*10) + self.shot_letter) + -1] = "o"
                        self.ship_field_2[(self.shot_number - 1 + (10 * self.ship_length) + self.shot_letter)] = "o"
                    elif self.shot_number == 1 and (self.shot_letter / 10) + self.ship_length == 10:
                        self.ship_field_2[(self.shot_number - 1 + (i*10) + self.shot_letter) + 1] = "o"
                        self.ship_field_2[(self.shot_number - 1 - 10 + self.shot_letter)] = "o"
                    elif self.shot_number != 1 and self.shot_number != 10 and (self.shot_letter / 10) + self.ship_length == 10:
                        self.ship_field_2[(self.shot_number - 1 + (i*10) + self.shot_letter) - 1] = "o"
                        self.ship_field_2[(self.shot_number - 1 + (i*10) + self.shot_letter) + 1] = "o"
                        self.ship_field_2[(self.shot_number - 1 - 10 + self.shot_letter)] = "o"
                    elif self.shot_number == 10 and (self.shot_letter / 10) + self.ship_length == 10:
                        self.ship_field_2[(self.shot_number - 1 + (i*10) + self.shot_letter) - 1] = "o"
                        self.ship_field_2[(self.shot_number - 1 - 10 + self.shot_letter)] = "o"
                    elif self.shot_number != 1 and self.shot_number != 10 and self.shot_letter and self.shot_letter == 0:
                        self.ship_field_2[(self.shot_number - 1 + (i*10) + self.shot_letter) - 1] = "o"
                        self.ship_field_2[(self.shot_number - 1 + (i*10) + self.shot_letter) + 1] = "o"
                        self.ship_field_2[(self.shot_number - 1 + (10 * self.ship_length) + self.shot_letter)] = "o"
                    elif self.shot_number == 1 and self.shot_letter != 0 and (self.shot_letter / 10) + self.ship_length != 10:
                        self.ship_field_2[(self.shot_number - 1 + (i*10) + self.shot_letter) + 1] = "o"
                        self.ship_field_2[(self.shot_number - 1 - 10 + self.shot_letter)] = "o"
                        self.ship_field_2[(self.shot_number - 1 + (10 * self.ship_length) + self.shot_letter)] = "o"
                    elif self.shot_number == 10 and self.shot_letter != 0 and (self.shot_letter / 10) + self.ship_length != 10:
                        self.ship_field_2[(self.shot_number - 1 + (i*10) + self.shot_letter) - 1] = "o"
                        self.ship_field_2[(self.shot_number - 1 - 10 + self.shot_letter)] = "o"
                        self.ship_field_2[(self.shot_number - 1 + (10 * self.ship_length) + self.shot_letter)] = "o"
                
        self.get_ship_field()

    def place_all_ships(self):
        print(f"Now player {self.player} place your ships:")
        print(f"Place your {self.ship_length}-cell ship:")
        self.ship_length = 4
        self.place_ship()
        self.ship_length = 3
        for i in range(2):
            print(f"Place your {self.ship_length}-cell ship:")
            self.place_ship()
        self.ship_length = 2
        for i in range(3):
            print(f"Place your {self.ship_length}-cell ship:")
            self.place_ship()
        self.ship_length = 1
        for i in range(4):
            print(f"Place your {self.ship_length}-cell ship:")        
            self.place_ship()
        if self.player == 1:
            self.player = 2
            self.ship_length = 4
            self.get_play_field()
            self.place_all_ships()
    
    def shot(self):
        if self.player == 1:
            self.get_ship_field()
            self.get_shot_number()
            self.get_shot_letter()
            if self.ship_field_1[self.shot_number - 1 + self.shot_letter] == "X":
                print(f"You hit the ship!")
                self.ship_field_1[self.shot_number - 1 + self.shot_letter] = "x"
                self.play_field_1[self.shot_number - 1 + self.shot_letter] = "X"
                self.shot()
            elif self.ship_field_1[self.shot_number - 1 + self.shot_letter] == "o":
                print(f"You barely missed the ship!")
                self.play_field_1[self.shot_number - 1 + self.shot_letter] = "O"
            else:
                print(f"You missed the ship!")
                self.play_field_1[self.shot_number - 1 + self.shot_letter] = "o"
        else:
            self.get_ship_field()
            self.get_shot_number()
            self.get_shot_letter()
            if self.ship_field_2[self.shot_number - 1 + self.shot_letter] == "X":
                print(f"You hit the ship!")
                self.ship_field_2[self.shot_number - 1 + self.shot_letter] = "x"
                self.play_field_2[self.shot_number - 1 + self.shot_letter] = "X"
                self.shot()
            elif self.ship_field_2[self.shot_number - 1 + self.shot_letter] == "o":
                print(f"You barely missed the ship!")
                self.play_field_2[self.shot_number - 1 + self.shot_letter] = "O"
            else:
                print(f"You missed the ship!")
                self.play_field_2[self.shot_number - 1 + self.shot_letter] = "o"

    def check_win(self):
        if self.player == 1:
            if "X" not in self.ship_field_2:
                print(f"Player {self.player} wins!")
                return True
            else:
                return False
        else:
            if "X" not in self.ship_field_1:
                print(f"Player {self.player} wins!")
                return True
            else:
                return False
    
    def game(self):
        print("Welcome to the game!")
        game.get_ship_field()
        self.place_all_ships()
        while True:
            self.shot()
            if self.check_win():
                break
            self.player = 2
            self.shot()
            if self.check_win():
                break
            self.player = 1

game = ShipDestroyer()
game.game()