def solve(arr):
    ts_arr = [None]*len(arr)
    ts_arr[::2] = sorted(arr[::2])
    ts_arr[1::2] = sorted(arr[1::2])
    for i in range(len(ts_arr)-1):
        if ts_arr[i] > ts_arr[i+1]:
            return i
    return 'OK'


if __name__ == '__main__':
    t = int(input())
    for x in range(1, t+1):
        n = int(input())
        arr = list(map(int, input().split()))
        ans = solve(arr)
        print('Case #{}: {}'.format(x, ans))
