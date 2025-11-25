def print_grid(grid):
    print("---------")
    for row in grid:
        print("|", " ".join(row), "|")
    print("---------")


def check_state(grid):
    lines = []

    # рядки
    lines.extend(grid)
    # стовпці
    lines.extend([[grid[r][c] for r in range(3)] for c in range(3)])
    # діагоналі
    lines.append([grid[i][i] for i in range(3)])
    lines.append([grid[i][2 - i] for i in range(3)])

    x_win = any(line == ["X", "X", "X"] for line in lines)
    o_win = any(line == ["O", "O", "O"] for line in lines)

    flat = [cell for row in grid for cell in row]
    if x_win and o_win:
        return "Impossible"
    elif x_win:
        return "X wins"
    elif o_win:
        return "O wins"
    elif "_" in flat or " " in flat:
        return "Game not finished"
    else:
        return "Draw"


def main():
    grid = [[" " for _ in range(3)] for _ in range(3)]
    print_grid(grid)

    current = "X"

    while True:
        coords = input("Enter the coordinates:\n> ").split()

        if len(coords) != 2 or not all(c.isdigit() for c in coords):
            print("You should enter numbers!")
            continue

        x, y = map(int, coords)
        if x < 1 or x > 3 or y < 1 or y > 3:
            print("Coordinates should be from 1 to 3!")
            continue

        if grid[x - 1][y - 1] != " ":
            print("This cell is occupied! Choose another one!")
            continue

        grid[x - 1][y - 1] = current
        print_grid(grid)

        state = check_state(grid)
        if state in ["X wins", "O wins", "Draw", "Impossible"]:
            print(state)
            break

        current = "O" if current == "X" else "X"


if __name__ == "__main__":
    main()
