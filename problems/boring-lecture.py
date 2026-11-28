# https://coderun.yandex.ru/problem/boring-lecture

word = input().strip()
length = len(word)
counts = {}

for i, char in enumerate(word):
    counts[char] = counts.get(char, 0) + (i + 1) * (length - i)

for char in sorted(counts):
    print(f'{char}: {counts[char]}')
