# https://coderun.yandex.ru/problem/alien-genome

a = input().strip()
b = input().strip()

pairs_b = {b[i:i+2] for i in range(len(b) - 1)}
count = sum(a[i:i+2] in pairs_b for i in range(len(a) - 1))
print(count)
