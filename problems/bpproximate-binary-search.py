# https://coderun.yandex.ru/problem/bpproximate-binary-search

import sys
from bisect import bisect_left

data = list(map(int, sys.stdin.buffer.read().split()))
n, k = data[0], data[1]
numbers = data[2:2 + n]
queries = data[2 + n:2 + n + k]

for value in queries:
    position = bisect_left(numbers, value)

    if position == 0:
        answer = numbers[0]
    elif position == n:
        answer = numbers[-1]
    elif value - numbers[position - 1] <= numbers[position] - value:
        answer = numbers[position - 1]
    else:
        answer = numbers[position]

    print(answer)
