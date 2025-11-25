import random

def ask_initial_pencils():
    while True:
        s = input("How many pencils would you like to use:\n> ")
        if not s.isdigit():
            print("The number of pencils should be numeric")
            continue
        n = int(s)
        if n <= 0:
            print("The number of pencils should be positive")
            continue
        return n

def ask_first_player(players):
    while True:
        first = input(f"Who will be the first ({players[0]}, {players[1]}):\n> ")
        if first not in players:
            print(f"Choose between '{players[0]}' and '{players[1]}'")
            continue
        return first

def bot_move(pencils):
    r = pencils % 4
    if r == 0:
        return 3 if pencils >= 3 else pencils
    elif r == 3:
        return 2 if pencils >= 2 else 1
    elif r == 2:
        return 1
    else:
        # losing position: pick any valid 1..3 not exceeding pencils
        return random.choice([m for m in (1, 2, 3) if m <= pencils])

def human_move(pencils):
    while True:
        s = input("> ")
        if s not in ("1", "2", "3"):
            print("Possible values: '1', '2' or '3'")
            continue
        m = int(s)
        if m > pencils:
            print("Too many pencils were taken")
            continue
        return m

def main():
    players = ["John", "Jack"]  # John — користувач, Jack — бот
    pencils = ask_initial_pencils()
    first = ask_first_player(players)
    turn = players.index(first)

    while pencils > 0:
        print("|" * pencils)
        current = players[turn]
        print(f"{current}'s turn!")

        if current == "Jack":
            m = bot_move(pencils)
            print(m)
        else:
            m = human_move(pencils)

        pencils -= m
        if pencils == 0:
            print(f"{players[1 - turn]} won!")
            break
        turn = 1 - turn

if __name__ == "__main__":
    main()
