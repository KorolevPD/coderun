# https://coderun.yandex.ru/problem/histogram

import sys
from collections import Counter

text = sys.stdin.read()
counts = Counter(char for char in text if char not in ' \n\r')

characters = sorted(counts)
max_count = max(counts.values())

for level in range(max_count, 0, -1):
    row = ''.join('#' if counts[char] >= level else ' ' for char in characters)
    print(row)

print(''.join(characters))
