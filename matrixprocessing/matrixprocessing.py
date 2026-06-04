import sys
from copy import deepcopy

def read_size(prompt="Enter matrix size: > "):
    s = input(prompt).strip()
    parts = s.split()
    if len(parts) == 1:
        try:
            r = int(parts[0])
            c = int(input().strip())
            return r, c
        except:
            raise ValueError("Invalid size")
    if len(parts) >= 2:
        return int(parts[0]), int(parts[1])
    raise ValueError("Invalid size")

def read_matrix(rows, cols, prompt="Enter matrix:\n"):
    print(prompt, end="")
    mat = []
    for _ in range(rows):
        line = input("> ").strip()
        while line == "":
            line = input("> ").strip()
        parts = line.split()
        if len(parts) != cols:
            raise ValueError("Row does not have expected number of columns")
        row = [float(x) if ('.' in x or 'e' in x or 'E' in x) else float(x) for x in parts]
        mat.append(row)
    return mat

def print_matrix(mat):
    for row in mat:
        out = []
        for v in row:
            if abs(v - round(v)) < 1e-9:
                out.append(str(int(round(v))))
            else:
                s = f"{v:.2f}".rstrip('0').rstrip('.')
                out.append(s)
        print(" ".join(out))

def add_matrices(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return None
    rows, cols = len(a), len(a[0])
    res = [[a[i][j] + b[i][j] for j in range(cols)] for i in range(rows)]
    return res

def multiply_by_constant(a, k):
    return [[elem * k for elem in row] for row in a]

def multiply_matrices(a, b):
    if len(a[0]) != len(b):
        return None
    rows, cols, inner = len(a), len(b[0]), len(b)
    res = [[0.0]*cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            s = 0.0
            for t in range(inner):
                s += a[i][t] * b[t][j]
            res[i][j] = s
    return res

def transpose_main(a):
    return [list(row) for row in zip(*a)]

def transpose_side(a):
    rows, cols = len(a), len(a[0])
    res = [[0]*rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            res[cols-1-j][rows-1-i] = a[i][j]
    return res

def transpose_vertical(a):
    return [list(reversed(row)) for row in a]

def transpose_horizontal(a):
    return list(reversed(a))

def determinant(matrix):
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("Determinant requires square matrix")
    m = deepcopy(matrix)
    det = 1.0
    for i in range(n):
        pivot = i
        for r in range(i, n):
            if abs(m[r][i]) > abs(m[pivot][i]):
                pivot = r
        if abs(m[pivot][i]) < 1e-12:
            return 0.0
        if pivot != i:
            m[i], m[pivot] = m[pivot], m[i]
            det *= -1
        det *= m[i][i]
        for r in range(i+1, n):
            factor = m[r][i] / m[i][i]
            for c in range(i, n):
                m[r][c] -= factor * m[i][c]
    return det

def cofactor_matrix(a):
    n = len(a)
    cof = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            minor = [row[:j] + row[j+1:] for idx,row in enumerate(a) if idx != i]
            cof[i][j] = ((-1)**(i+j)) * determinant(minor)
    return cof

def inverse_matrix(a):
    n = len(a)
    if any(len(row) != n for row in a):
        raise ValueError("Inverse requires square matrix")
    det = determinant(a)
    if abs(det) < 1e-12:
        return None
    cof = cofactor_matrix(a)
    adj = transpose_main(cof)
    inv = [[adj[i][j] / det for j in range(n)] for i in range(n)]
    return inv

def menu():
    while True:
        print("\n1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")
        choice = input("Your choice: > ").strip()
        if choice == "0":
            break
        if choice == "1":
            try:
                r1, c1 = read_size("Enter size of first matrix: > ")
                a = read_matrix(r1, c1, "Enter first matrix:\n")
                r2, c2 = read_size("Enter size of second matrix: > ")
                b = read_matrix(r2, c2, "Enter second matrix:\n")
                res = add_matrices(a, b)
                if res is None:
                    print("The operation cannot be performed.")
                else:
                    print("The result is:")
                    print_matrix(res)
            except Exception:
                print("ERROR")
        elif choice == "2":
            try:
                r, c = read_size("Enter size of matrix: > ")
                a = read_matrix(r, c, "Enter matrix:\n")
                k_line = input("Enter constant: > ").strip()
                k = float(k_line)
                res = multiply_by_constant(a, k)
                print("The result is:")
                print_matrix(res)
            except Exception:
                print("ERROR")
        elif choice == "3":
            try:
                r1, c1 = read_size("Enter size of first matrix: > ")
                a = read_matrix(r1, c1, "Enter first matrix:\n")
                r2, c2 = read_size("Enter size of second matrix: > ")
                b = read_matrix(r2, c2, "Enter second matrix:\n")
                res = multiply_matrices(a, b)
                if res is None:
                    print("The operation cannot be performed.")
                else:
                    print("The result is:")
                    print_matrix(res)
            except Exception:
                print("ERROR")
        elif choice == "4":
            print("\n1. Main diagonal")
            print("2. Side diagonal")
            print("3. Vertical line")
            print("4. Horizontal line")
            t = input("Your choice: > ").strip()
            try:
                r, c = read_size("Enter matrix size: > ")
                a = read_matrix(r, c, "Enter matrix:\n")
                if t == "1":
                    res = transpose_main(a)
                elif t == "2":
                    res = transpose_side(a)
                elif t == "3":
                    res = transpose_vertical(a)
                elif t == "4":
                    res = transpose_horizontal(a)
                else:
                    print("Invalid transpose option.")
                    continue
                print("The result is:")
                print_matrix(res)
            except Exception:
                print("ERROR")
        elif choice == "5":
            try:
                r, c = read_size("Enter matrix size: > ")
                if r != c:
                    print("The operation cannot be performed.")
                    continue
                a = read_matrix(r, c, "Enter matrix:\n")
                det = determinant(a)
                if abs(det - round(det)) < 1e-9:
                    print(int(round(det)))
                else:
                    s = f"{det:.2f}".rstrip('0').rstrip('.')
                    print(s)
            except Exception:
                print("ERROR")
        elif choice == "6":
            try:
                r, c = read_size("Enter matrix size: > ")
                if r != c:
                    print("This matrix doesn't have an inverse.")
                    continue
                a = read_matrix(r, c, "Enter matrix:\n")
                inv = inverse_matrix(a)
                if inv is None:
                    print("This matrix doesn't have an inverse.")
                else:
                    print("The result is:")
                    print_matrix(inv)
            except Exception:
                print("ERROR")

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        sys.exit(0)
