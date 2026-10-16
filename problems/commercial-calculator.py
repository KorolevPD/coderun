# https://coderun.yandex.ru/problem/commercial-calculator

import heapq

n = int(input())
a = list(map(int, input().split()))

heapq.heapify(a)
total_cost = 0.0

while len(a) > 1:
    x = heapq.heappop(a)
    y = heapq.heappop(a)
    s = x + y
    total_cost += s * 0.05
    heapq.heappush(a, s)

print(f"{total_cost:.2f}")
