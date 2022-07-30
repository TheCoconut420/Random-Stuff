from traceback import print_tb


class ShipDestroyer:
    def __init__(self):
        self.wave = " "
        self.play_field_1  = [self.wave] * 100
        self.play_field_2 = [self.wave] * 100 
        self.ship_field_1  = [self.wave] * 100 
        self.ship_field_2 = [self.wave] * 100
        self.player_count = 2
        self.player = 1
        self.ship_length = 0

    def print_play_field(self):
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

    def print_ship_field(self):
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
            self.shot_letter = 1
        elif self.shot_letter == "C":
            self.shot_letter = 2
        elif self.shot_letter == "D":
            self.shot_letter = 3
        elif self.shot_letter == "E":
            self.shot_letter = 4
        elif self.shot_letter == "F":
            self.shot_letter = 5
        elif self.shot_letter == "G":
            self.shot_letter = 6
        elif self.shot_letter == "H":
            self.shot_letter = 7
        elif self.shot_letter == "I":
            self.shot_letter = 8
        elif self.shot_letter == "J":
            self.shot_letter = 9
        else:
            print("You entered an invalid letter!")
            self.get_shot_letter()
        if self.rotate == "y":
            if self.shot_letter + self.ship_length > 10:
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

    def place_ship(self):
        print("The ship will be placed from left to right.")
        print("For example, if you place the ship on A1, it will be placed on A1, A2, A3, A4.")
        print("You can also rotate the ship by 90° degrees.")
        print("Then it will be placed on A1, B1, C1, D1.")
        if self.player == 1:
            self.print_play_field()
            print("")
            print("Now you will place the 4-tile ship on the play field.")
            self.rotate = input("Do you want to turn the ship 90° degrees? (y/n): ")
            print("Where do you want to place the 4-tile ship?")
            self.ship_length = 4
            self.get_shot_letter()
            self.get_shot_number()
            
                
game = ShipDestroyer()
game.place_ship()