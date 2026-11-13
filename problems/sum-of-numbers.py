# https://coderun.yandex.ru/problem/sum-of-numbers

import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n, k = data[0], data[1]
numbers = data[2:2 + n]

prefix_count = {0: 1}
prefix_sum = 0
answer = 0

for number in numbers:
    prefix_sum += number
    answer += prefix_count.get(prefix_sum - k, 0)
    prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

print(answer)
