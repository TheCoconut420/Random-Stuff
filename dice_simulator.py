import time
import random # Import the random module

class dice:
    def __init__(self):
        self.amount = ""
        self.dice_amount = ""
        self.sum = 0
        self.dice_side = ""
        self.dice_list = []
        self.trys = 0
        self.average = 0
        self.sort_results = ""
    
    def infos(self):
        self.dice_amount = int(input("How many dice do you want to roll?: "))
        if self.dice_amount <= 0:
            print("The amount of dice can't be lower than 1")
            self.infos()
        else:
            self.dice_side = int(input("How many sides do you want the dice to have?: "))
            if self.dice_side <= 0:
                print("The amount of sides can't be lower than 1")
                self.infos()
        choose = input("Do you want to wait for a specific result? (y/n): ")
        if choose == "y":
            user_try = int(input("What sum do you want to get?: "))
            if user_try < self.dice_amount:
                print("The sum can't be lower than " + str(self.dice_amount))
                self.infos()
            elif user_try > self.dice_side * self.dice_amount:
                print("The sum can't be higher than " + str(self.dice_side * self.dice_amount))
                print("\n")
                self.infos()
            else:
                self.roll_for_result(user_try)

        else:
            self.sort_results = input("Do you want to sort the results? (y/n): ")
            self.roll_dice()
            self.show_results()

    def roll_for_result(self, user_try):
        start = time.time()
        while self.sum != user_try:
            self.sum = 0
            self.roll_dice()
            self.trys += 1
        end = time.time()
        print("You got the sum in " + str(self.trys) + " tries")
        print("It took " + str(end - start) + " seconds")
        print("")
        choose = input("Do you want to try it again? (y/n): ")
        if choose == "y":
            print("\n")
            self.sum = 0
            self.trys = 0
            self.roll_for_result(user_try)
        else:
            print("Goodbye!")

    def roll_dice(self):
        for i in range(self.dice_amount):
            self.amount = random.randint(1, self.dice_side)
            self.dice_list.append(self.amount)
            self.sum += self.amount
        self.average = ((self.dice_side + 1) / 2) * self.dice_amount

    def show_results(self):
        if self.sort_results == "y":
            self.dice_list.sort()
        print("")
        print("You rolled: ")
        print(self.dice_list)
        print("The sum of the dice is: " + str(self.sum))
        print("The average of the dice is: " + str(self.average))
        print("")
        choose = input("Do you want to roll again? (y/n): ")
        if choose == "y":
            self.dice_list = []
            self.sum = 0
            self.trys = 0
            self.average = 0
            self.roll_dice()
            self.show_results()
        else:
            print("")
            print("Thanks for using the dice simulator!")
            print("")
            exit()

print("\n")
print("Welcome to the dice simulator!")
dice_simulator = dice()
dice_simulator.infos()