# https://coderun.yandex.ru/problem/cleaning-day

import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n, r, c = data[0], data[1], data[2]
heights = sorted(data[3:3 + n])


def can_form(max_difference):
    groups = 0
    i = 0

    while i + c <= n:
        if heights[i + c - 1] - heights[i] <= max_difference:
            groups += 1
            i += c
        else:
            i += 1

    return groups >= r


low = -1
high = heights[-1] - heights[0]

while high - low > 1:
    middle = (low + high) // 2
    if can_form(middle):
        high = middle
    else:
        low = middle

print(high)
