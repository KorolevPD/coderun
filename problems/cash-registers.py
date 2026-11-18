# https://coderun.yandex.ru/problem/cash-registers

n = int(input())
difference = [0] * 1441

for _ in range(n):
    open_hour, open_minute, close_hour, close_minute = map(int, input().split())
    start = open_hour * 60 + open_minute
    end = close_hour * 60 + close_minute

    if start == end:
        difference[0] += 1
        difference[1440] -= 1
    elif start < end:
        difference[start] += 1
        difference[end] -= 1
    else:
        difference[start] += 1
        difference[1440] -= 1
        difference[0] += 1
        difference[end] -= 1

coverage = 0
answer = 0

for minute in range(1440):
    coverage += difference[minute]
    if coverage == n:
        answer += 1

print(answer)
