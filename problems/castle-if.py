# https://coderun.yandex.ru/problem/castle-if

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

brick = sorted([a, b, c])
hole = sorted([d, e])

if brick[0] <= hole[0] and brick[1] <= hole[1]:
    print('YES')
else:
    print('NO')
