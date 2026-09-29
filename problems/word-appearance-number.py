# https://coderun.yandex.ru/problem/word-appearance-number

from collections import defaultdict

count: defaultdict = defaultdict(int)
with open('input.txt', 'r') as fin, open('output.txt', 'w') as fout:
    for line in fin:
        for word in line.strip().split():
            fout.write(str(count[word]) + ' ')
            count[word] += 1
