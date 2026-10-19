# https://coderun.yandex.ru/problem/cutting-of-bars

L, N = map(int, input().split())
cuts = [0] + list(map(int, input().split())) + [L]
dp = [[0] * (N + 2) for _ in range(N + 2)]

for length in range(2, N + 2):
    for i in range(0, N + 2 - length):
        j = i + length
        dp[i][j] = min(
            dp[i][k] + dp[k][j] for k in range(i + 1, j)
        ) + cuts[j] - cuts[i]

print(dp[0][N + 1])
