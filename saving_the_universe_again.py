def min_swaps(total_damage, string):
    min_damage = string.count('S')
    if min_damage > total_damage:
        return 'IMPOSSIBLE'

    max_damage = 0
    pwr = 1
    for e in string:
        if e == 'S':
            max_damage += pwr
        else:
            pwr *= 2

    if max_damage <= total_damage:
        return 0

    s_so_far = 0
    swaps = 0
    for e in reversed(string):
        if e == 'S':
            s_so_far += 1
        else:
            pwr //= 2
            tmp = s_so_far*pwr
            if max_damage - tmp > total_damage:
                swaps += s_so_far
                max_damage -= tmp
            else:
                swaps += abs(-(max_damage-total_damage)//pwr)
                break
    return swaps


if __name__ == '__main__':
    t = int(input())
    for x in range(1, t + 1):
        td, s = input().strip().split()
        D = int(td)
        ans = min_swaps(td, s)
        print('Case #{}: {}'.format(x, ans))
