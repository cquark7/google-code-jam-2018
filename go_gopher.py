def solve():
    for i, j in boxes:
        guessed = set()
        grid = ((x, y) for x in range(i-1, i+2) for y in range(j-1, j+2))
        grid = set(grid)
        while guessed != grid:
            print(i, j)
            m, n = map(int, input().split())
            if m == 0:
                return
            guessed.add((m, n))


if __name__ == '__main__':
    t = int(input())
    boxes = [(2, c) for c in range(2, 70, 3)]
    for x in range(t):
        area = int(input())
        solve()
