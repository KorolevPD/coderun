# https://coderun.yandex.ru/problem/determine-type-sequence

import sys

numbers = []
for value in map(int, sys.stdin.buffer.read().split()):
    if value == -2_000_000_000:
        break
    numbers.append(value)

if len(numbers) <= 1 or all(x == numbers[0] for x in numbers):
    print('CONSTANT')
elif all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1)):
    print('ASCENDING')
elif all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1)):
    print('WEAKLY ASCENDING')
elif all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1)):
    print('DESCENDING')
elif all(numbers[i] >= numbers[i + 1] for i in range(len(numbers) - 1)):
    print('WEAKLY DESCENDING')
else:
    print('RANDOM')
