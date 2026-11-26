# https://coderun.yandex.ru/problem/good-line

import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
counts = data[1:1 + n]

answer = 0

for i in range(n - 1):
    answer += min(counts[i], counts[i + 1])

print(answer)
