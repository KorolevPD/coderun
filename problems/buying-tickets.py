# https://coderun.yandex.ru/problem/buying-tickets

n = int(input())
A = [0] * (n + 1)
B = [0] * (n + 1)
C = [0] * (n + 1)

for i in range(1, n + 1):
    a, b, c = map(int, input().split())
    A[i] = a
    B[i] = b
    C[i] = c

INF = float('inf')
dp = [INF] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    dp[i] = min(dp[i], dp[i - 1] + A[i])
    if i >= 2:
        dp[i] = min(dp[i], dp[i - 2] + B[i - 1])
    if i >= 3:
        dp[i] = min(dp[i], dp[i - 3] + C[i - 2])

print(dp[n])
