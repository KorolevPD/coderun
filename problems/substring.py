# https://coderun.yandex.ru/problem/substring

import sys

data = sys.stdin.buffer.read().split()
n = int(data[0])
k = int(data[1])
text = data[2].decode()

counts = {}
left = 0
best_length = 0
best_start = 0

for right in range(n):
    char = text[right]
    counts[char] = counts.get(char, 0) + 1

    while counts[char] > k:
        left_char = text[left]
        counts[left_char] -= 1
        left += 1

    length = right - left + 1
    if length > best_length:
        best_length = length
        best_start = left

print(best_length, best_start + 1)
