# https://coderun.yandex.ru/problem/print-the-route-of-the-maximum-cost

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]
dp[0][0] = a[0][0]

for j in range(1, m):
    dp[0][j] = dp[0][j - 1] + a[0][j]

for i in range(1, n):
    dp[i][0] = dp[i - 1][0] + a[i][0]

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + a[i][j]

path = []
i, j = n - 1, m - 1
while i > 0 or j > 0:
    if i > 0 and (j == 0 or dp[i - 1][j] >= dp[i][j - 1]):
        path.append('D')
        i -= 1
    else:
        path.append('R')
        j -= 1

path.reverse()
print(dp[n - 1][m - 1])
print(''.join(path))
