class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.state = "main"

    def print_state(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")

    def can_make(self, water, milk, beans):
        if self.water < water:
            print("Sorry, not enough water!")
            return False
        if self.milk < milk:
            print("Sorry, not enough milk!")
            return False
        if self.beans < beans:
            print("Sorry, not enough coffee beans!")
            return False
        if self.cups < 1:
            print("Sorry, not enough cups!")
            return False
        print("I have enough resources, making you a coffee!")
        return True

    def buy(self):
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:\n> ")
        if choice == "back":
            return
        if choice == "1":  # espresso
            if self.can_make(250, 0, 16):
                self.water -= 250
                self.beans -= 16
                self.cups -= 1
                self.money += 4
        elif choice == "2":  # latte
            if self.can_make(350, 75, 20):
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cups -= 1
                self.money += 7
        elif choice == "3":  # cappuccino
            if self.can_make(200, 100, 12):
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                self.money += 6

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:\n> "))
        self.milk += int(input("Write how many ml of milk do you want to add:\n> "))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:\n> "))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:\n> "))

    def take(self):
        print(f"I gave you {self.money}")
        self.money = 0

    def process(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):\n> ")
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.print_state()
            elif action == "exit":
                break


if __name__ == "__main__":
    machine = CoffeeMachine()
    machine.process()
