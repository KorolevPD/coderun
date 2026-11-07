# https://coderun.yandex.ru/problem/number-different-numbers

import sys

numbers = list(map(int, sys.stdin.buffer.read().split()))
print(len(set(numbers)))
