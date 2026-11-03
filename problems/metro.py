# https://coderun.yandex.ru/problem/metro

a = int(input())
b = int(input())
n = int(input())
m = int(input())

first_period = a + 1
second_period = b + 1

minimum = max((n - 1) * first_period + 1, (m - 1) * second_period + 1)
maximum = min((n + 1) * first_period - 1, (m + 1) * second_period - 1)

if minimum <= maximum:
    print(minimum, maximum)
else:
    print(-1)
