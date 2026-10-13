# https://coderun.yandex.ru/problem/more-your-neighbors

n = list(map(int, input().split()))
print(sum(n[i - 1] < n[i] > n[i + 1] for i in range(1, len(n) - 1)))
