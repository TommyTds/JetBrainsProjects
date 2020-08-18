class CoffeeMachine:
    money = 550
    water = 400
    milk = 540
    coffee = 120
    cups = 9

    def __init__(self):
        pass

    def manipulator(self, action):
        if action == "buy":
            self.buy()
            return
        elif action == "fill":
            self.fill()
            return
        elif action == "take":
            self.take()
            return
        elif action == "remaining":
            self.remaining()
            return
        elif action == "exit":
            return

    def remaining(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.coffee, "of coffee beans")
        print(self.cups, "of disposable cups")
        print(self.money, "of money")

    def buy(self):
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if choice == "back":
            return
        elif choice == "1":
            if self.water < 250:
                print("Sorry, not enough water!")
                return
            if self.coffee < 16:
                print("Sorry, not enough coffee!")
                return
            if self.cups < 1:
                print("Sorry, not enough cups!")
                return
            print("I have enough resources, making you a coffee!")
            self.water -= 250
            self.coffee -= 16
            self.cups -= 1
            self.money += 4

        elif choice == "2":
            if self.water < 350:
                print("Sorry, not enough water!")
                return
            if self.coffee < 20:
                print("Sorry, not enough coffee!")
                return
            if self.milk < 75:
                print("Sorry, not enough milk!")
                return
            if self.cups < 1:
                print("Sorry, not enough cups!")
                return
            print("I have enough resources, making you a coffee!")
            self.water -= 350
            self.milk -= 75
            self.coffee -= 20
            self.cups -= 1
            self.money += 7

        elif choice == "3":
            if self.water < 200:
                print("Sorry, not enough water!")
                return
            if self.coffee < 12:
                print("Sorry, not enough coffee!")
                return
            if self.milk < 100:
                print("Sorry, not enough milk!")
                return
            if self.cups < 1:
                print("Sorry, not enough cups!")
            print("I have enough resources, making you a coffee!")
            self.water -= 200
            self.milk -= 100
            self.coffee -= 12
            self.cups -= 1
            self.money += 6


    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.coffee += int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:"))


    def take(self):
        self.money = 0


coffee = CoffeeMachine()


while True:
    action = input("Write action (buy, fill, take, remaining, exit):")
    if action == "exit":
        break
    coffee.manipulator(action)

"""actual_water = int(input("Write how many ml of water the coffee machine has: "))
actual_milk = int(input("Write how many ml of milk the coffee machine has: "))
actual_beans = int(input("Write how many grams of coffee beans the coffee machine has: "))
cups_number = int(input("Write how many cups of coffee you will need: "))

possible_cups_water = actual_water // 200
possible_cups_milk = actual_milk // 50
possible_cups_beans = actual_beans // 15

deciding_factor = ""
if possible_cups_water <= possible_cups_milk and possible_cups_water <= possible_cups_beans:
    deciding_factor = "water"
elif possible_cups_milk <= possible_cups_water and possible_cups_milk <= possible_cups_beans:
    deciding_factor = "milk"
else:
    deciding_factor = "beans"

if deciding_factor == "water":
    possible_cups = actual_water // 200
    if possible_cups == cups_number:
        print("Yes, I can make that amount of coffee")
    elif possible_cups > cups_number:
        print("Yes, I can make that amount of coffee (and even ", possible_cups - cups_number, "more than that)")
    else:
        print("No, I can make only ", possible_cups, "cups of coffee")
elif deciding_factor == "milk":
    possible_cups = actual_milk // 50
    if possible_cups == cups_number:
        print("Yes, I can make that amount of coffee")
    elif possible_cups > cups_number:
        print("Yes, I can make that amount of coffee (and even ", possible_cups - cups_number, "more than that)")
    else:
        print("No, I can make only ", possible_cups, "cups of coffee")
elif deciding_factor == "beans":
    possible_cups = actual_beans // 15
    if possible_cups == cups_number:
        print("Yes, I can make that amount of coffee")
    elif possible_cups > cups_number:
        print("Yes, I can make that amount of coffee (and even ", possible_cups - cups_number, "more than that)")
    else:
        print("No, I can make only ", possible_cups, "cups of coffee")"""
