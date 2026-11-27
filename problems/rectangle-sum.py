# https://coderun.yandex.ru/problem/rectangle-sum

import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n, m, k = data[0], data[1], data[2]

prefix = [[0] * (m + 1) for _ in range(n + 1)]
index = 3

for i in range(1, n + 1):
    for j in range(1, m + 1):
        value = data[index]
        index += 1
        prefix[i][j] = (prefix[i - 1][j] + prefix[i][j - 1]
                        - prefix[i - 1][j - 1] + value)

for _ in range(k):
    x1 = data[index]
    y1 = data[index + 1]
    x2 = data[index + 2]
    y2 = data[index + 3]
    index += 4

    answer = (prefix[x2][y2] - prefix[x1 - 1][y2]
              - prefix[x2][y1 - 1] + prefix[x1 - 1][y1 - 1])
    print(answer)
