# https://coderun.yandex.ru/problem/number-of-triangles

n = int(input())
if n % 2 == 0:
    total = n * (n + 2) * (2 * n + 1) // 8
else:
    total = (n * (n + 2) * (2 * n + 1) - 1) // 8
print(total)
