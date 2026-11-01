# https://coderun.yandex.ru/problem/toy-maze

import sys
from collections import deque

data = sys.stdin.buffer.read().split()
n = int(data[0])
m = int(data[1])

maze = []
index = 2
for _ in range(n):
    maze.append([int(x) for x in data[index:index + m]])
    index += m

visited = [[False] * m for _ in range(n)]
visited[0][0] = True
queue = deque([(0, 0, 0)])
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = -1

while queue and answer == -1:
    x, y, distance = queue.popleft()

    for dx, dy in directions:
        nx, ny = x, y
        fell = False

        while True:
            tx, ty = nx + dx, ny + dy
            if not (0 <= tx < n and 0 <= ty < m):
                break
            if maze[tx][ty] == 1:
                break

            nx, ny = tx, ty
            if maze[nx][ny] == 2:
                answer = distance + 1
                fell = True
                break

        if fell:
            break

        if (nx, ny) != (x, y) and not visited[nx][ny]:
            visited[nx][ny] = True
            queue.append((nx, ny, distance + 1))

print(answer)
