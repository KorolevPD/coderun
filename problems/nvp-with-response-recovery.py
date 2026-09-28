# https://coderun.yandex.ru/problem/nvp-with-response-recovery

count = [1] * int(input())
prev = [-1] * len(count)
sequence = list(map(int, input().split()))

for i in range(1, len(sequence)):
    for j in range(i):
        if sequence[j] < sequence[i] and count[j] + 1 > count[i]:
            count[i] = count[j] + 1
            prev[i] = j


max_len = max(count)
idx = count.index(max_len)
lcs = []
while idx != -1:
    lcs.append(sequence[idx])
    idx = prev[idx]

print(*reversed(lcs))
