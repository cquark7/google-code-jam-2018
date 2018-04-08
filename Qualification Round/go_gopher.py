def gopher():
    for i, j in cells:
        filled = set()
        while len(filled) < 9:
            print(i, j)
            m, n = map(int, input().split())
            if m == 0:
                return
            filled.add((m, n))


if __name__ == '__main__':
    t = int(input())
    cells = [(2, c) for c in range(2, 70, 3)]
    for x in range(t):
        area = int(input())
        gopher()
