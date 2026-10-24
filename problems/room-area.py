# https://coderun.yandex.ru/problem/room-area

n = int(input())
maze = [list(input().strip()) for _ in range(n)]
r, c = map(int, input().split())

r -= 1
c -= 1

visited = [[False] * n for _ in range(n)]
stack = [(r, c)]
visited[r][c] = True
count = 0

while stack:
    x, y = stack.pop()
    count += 1
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if (0 <= nx < n and 0 <= ny < n and not visited[nx][ny]
                and maze[nx][ny] == "."):
            visited[nx][ny] = True
            stack.append((nx, ny))

print(count)
