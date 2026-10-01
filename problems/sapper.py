# https://coderun.yandex.ru/problem/sapper

n, m, k = map(int, input().split())
field = [[0] * m for _ in range(n)]
moves = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if x or y]

for _ in range(k):
    x, y = (int(i) - 1 for i in input().split())
    field[x][y] = '*'  # type: ignore
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and field[nx][ny] != '*':
            field[nx][ny] += 1

for row in field:
    print(*row)
