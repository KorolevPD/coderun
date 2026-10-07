# https://coderun.yandex.ru/problem/conditioner

tr, tc = map(int, input().split())
mode = input()

if mode == 'freeze':
    print(min(tr, tc))
elif mode == 'heat':
    print(max(tr, tc))
elif mode == 'auto':
    print(tc)
else:
    print(tr)
