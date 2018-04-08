# Note: Solution is partially correct
# To Do: Update solution

def solve(area):
    sin = (area + pow(2 - area*area, 0.5)) / 2
    cos = (area - pow(2 - area*area, 0.5)) / 2
    print(0, 0, 0.5)
    print(0.5*cos, 0.5*sin, 0)
    print(-0.5*sin, 0.5*cos, 0)


if __name__ == '__main__':
    t = int(input())
    for x in range(1, t + 1):
        a = float(input())
        print('Case #{}:'.format(x))
        solve(a)
