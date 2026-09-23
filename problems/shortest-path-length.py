# https://coderun.yandex.ru/problem/shortest-path-length

from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
start, end = [int(i) - 1 for i in input().split()]

visited = [False] * n
dist = [-1] * n

queue = deque([start])
visited[start] = True
dist[start] = 0

while queue:
    v = queue.popleft()
    if v == end:
        print(dist[v])
        break
    for u, connected in enumerate(graph[v]):
        if connected and not visited[u]:
            visited[u] = True
            dist[u] = dist[v] + 1
            queue.append(u)
else:
    print(-1)
