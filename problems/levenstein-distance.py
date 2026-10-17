# https://coderun.yandex.ru/problem/levenstein-distance

s1 = input().strip()
s2 = input().strip()

if len(s1) < len(s2):
    s1, s2 = s2, s1

n, m = len(s1), len(s2)
prev = list(range(m + 1))

for i in range(1, n + 1):
    curr = [i] + [0] * m
    c1 = s1[i-1]
    for j in range(1, m + 1):
        cost = 0 if c1 == s2[j-1] else 1
        curr[j] = min(
            prev[j] + 1,
            curr[j-1] + 1,
            prev[j-1] + cost
        )
    prev = curr

print(prev[m])
