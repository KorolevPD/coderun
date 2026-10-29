# https://coderun.yandex.ru/problem/two-horses

from collections import deque


def pos_to_coords(p):
    x = ord(p[0]) - ord('a')
    y = int(p[1]) - 1
    return x, y


moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
         (-2, -1), (-1, -2), (1, -2), (2, -1)]


def bfs(start):
    dist = [[-1]*8 for _ in range(8)]
    x, y = start
    dist[x][y] = 0
    q = deque([(x, y)])
    while q:
        cx, cy = q.popleft()
        for dx, dy in moves:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < 8 and 0 <= ny < 8 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[cx][cy] + 1
                q.append((nx, ny))
    return dist


p1, p2 = input().split()
r = pos_to_coords(p1)
g = pos_to_coords(p2)

dist_r = bfs(r)
dist_g = bfs(g)

best = -1
for i in range(8):
    for j in range(8):
        dr = dist_r[i][j]
        dg = dist_g[i][j]
        if dr == -1 or dg == -1:
            continue
        if (dr % 2) == (dg % 2):
            t = max(dr, dg)
            if best == -1 or t < best:
                best = t

print(best)
