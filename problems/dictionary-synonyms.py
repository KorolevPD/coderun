# https://coderun.yandex.ru/problem/dictionary-synonyms

dictionary = dict(input().split() for _ in range(int(input())))
query = input()

for k, v in dictionary.items():
    if query in (k, v):
        print(v if k == query else k)
        break
