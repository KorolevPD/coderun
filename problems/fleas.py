# https://coderun.yandex.ru/problem/fleas

from collections import deque


def get_possible_dirs(v, field_size):
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
             (-2, -1), (-1, -2), (1, -2), (2, -1)]
    for dx, dy in moves:
        nx, ny = v[0] + dx, v[1] + dy
        if 1 <= nx <= field_size[0] and 1 <= ny <= field_size[1]:
            yield (nx, ny)


def bfs(end, n, m):
    dist = [[-1]*(m+1) for _ in range(n+1)]
    queue = deque([end])
    dist[end[0]][end[1]] = 0

    while queue:
        x, y = queue.popleft()
        for nx, ny in get_possible_dirs((x, y), (n, m)):
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
    return dist


def main():
    n, m, s, t, q = map(int, input().split())
    end = (s, t)
    dist_map = bfs(end, n, m)

    total_dist = 0
    for _ in range(q):
        start = tuple(map(int, input().split()))
        d = dist_map[start[0]][start[1]]
        if d == -1:
            print(-1)
            return
        total_dist += d

    print(total_dist)


if __name__ == '__main__':
    main()
