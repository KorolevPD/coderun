# https://coderun.yandex.ru/problem/pyramid

n = int(input())
best_height = {}

for _ in range(n):
    width, height = map(int, input().split())
    if width not in best_height or height > best_height[width]:
        best_height[width] = height

print(sum(best_height.values()))
