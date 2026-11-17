# https://coderun.yandex.ru/problem/median-union

import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n, length = data[0], data[1]

sequences = []
index = 2
for _ in range(n):
    sequences.append(data[index:index + length])
    index += length


def left_median(first, second):
    i = 0
    j = 0
    value = 0

    for _ in range(length):
        if j == length or (i < length and first[i] <= second[j]):
            value = first[i]
            i += 1
        else:
            value = second[j]
            j += 1

    return value


for i in range(n):
    for j in range(i + 1, n):
        print(left_median(sequences[i], sequences[j]))
