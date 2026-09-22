# https://coderun.yandex.ru/problem/knight-move

n, m = map(int, input().split())
field = [[0] * m for _ in range(n)]

field[0][0] = 1

for i in range(n):
    for j in range(m):
        if i >= 2 and j >= 1:
            field[i][j] += field[i-2][j-1]
        if i >= 1 and j >= 2:
            field[i][j] += field[i-1][j-2]

print(field[-1][-1])
