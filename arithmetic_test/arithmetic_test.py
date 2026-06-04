import random
import sys

def ask_integer(prompt="> "):
    while True:
        s = input(prompt).strip()
        try:
            return int(s)
        except ValueError:
            print("Incorrect format.")

def level_choice():
    while True:
        print("Which level do you want? Enter a number:")
        print("1 - simple operations with numbers 2-9")
        print("2 - integral squares of 11-29")
        choice = input("> ").strip()
        if choice in ("1", "2"):
            return int(choice)
        print("Incorrect format.")

def generate_question(level):
    if level == 1:
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        op = random.choice(['+', '-', '*'])
        expr = f"{a} {op} {b}"
        correct = eval(expr)
        prompt = expr
    else:
        n = random.randint(11, 29)
        expr = f"{n}"
        correct = n * n
        prompt = expr
    return prompt, correct

def run_test(level):
    score = 0
    for _ in range(5):
        prompt, correct = generate_question(level)
        print(prompt)
        ans = ask_integer()
        if ans == correct:
            print("Right!")
            score += 1
        else:
            print("Wrong!")
    print(f"Your mark is {score}/5.")
    return score

def save_result(score, level):
    mapping = {
        1: "simple operations with numbers 2-9",
        2: "integral squares of 11-29"
    }
    print("Would you like to save your result to the file? Enter yes or no.")
    resp = input("> ").strip()
    if resp in ("yes", "YES", "y", "Yes"):
        print("What is your name?")
        name = input("> ").strip()
        line = f"{name}: {score}/5 in level {level} ({mapping[level]})\n"
        with open("results.txt", "a", encoding="utf-8") as f:
            f.write(line)
        print('The results are saved in "results.txt".')

def main():
    level = level_choice()
    score = run_test(level)
    save_result(score, level)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
