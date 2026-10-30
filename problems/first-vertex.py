# https://coderun.yandex.ru/problem/first-vertex

n, m = map(int, input().split())

rev = [[] for _ in range(n + 1)]  # type: ignore
for _ in range(m):
    u, v = map(int, input().split())
    rev[v].append(u)

visited = [False] * (n + 1)
visited[1] = True
stack = [1]

while stack:
    v = stack.pop()
    for u in rev[v]:
        if not visited[u]:
            visited[u] = True
            stack.append(u)

result = [str(i) for i in range(1, n + 1) if visited[i]]
print(' '.join(result))
