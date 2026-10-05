def solve_queens(n):
    solutions = []
    cols = []

    def safe(row, col):
        for r in range(row):
            c = cols[r]

            if c == col or abs(c - col) == abs(r - row):
                return False

        return True

    def place(row):
        if row == n:
            solutions.append(cols[:])
            return

        for col in range(n):
            if safe(row, col):
                cols.append(col)
                place(row + 1)
                cols.pop()

    place(0)

    return solutions


sols = solve_queens(4)

print("4-Queens solutions:", len(sols))

for s in sols:
    print(s)

    for r in range(4):
        print(" ".join("Q" if c == s[r] else "." for c in range(4)))

    print()

print("6-Queens solutions:", len(solve_queens(6)))
print("8-Queens solutions:", len(solve_queens(8)))
