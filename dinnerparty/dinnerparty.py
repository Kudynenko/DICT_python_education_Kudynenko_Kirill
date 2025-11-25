import random

print("Enter the number of friends joining (including you):")
num = int(input("> "))

if num <= 0:
    print("No one is joining for the party")
else:
    friends = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(num):
        name = input("> ")
        friends[name] = 0

    total = int(input("Enter the total amount:\n> "))
    share = round(total / num, 2)
    for name in friends:
        friends[name] = share

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    choice = input("> ")

    if choice == "Yes":
        lucky = random.choice(list(friends.keys()))
        print(f"{lucky} is the lucky one!")
        new_share = round(total / (num - 1), 2)
        for name in friends:
            friends[name] = new_share
        friends[lucky] = 0
    else:
        print("No one is going to be lucky")

    print(friends)
