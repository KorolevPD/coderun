# https://coderun.yandex.ru/problem/intersection-sets

import sys

lines = sys.stdin.read().splitlines()
first = set(map(int, lines[0].split()))
second = set(map(int, lines[1].split()))

print(*sorted(first & second))
