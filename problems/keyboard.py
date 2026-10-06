# https://coderun.yandex.ru/problem/keyboard

a = int(input())
keys_durability = [int(x) for x in input().split()]
b = int(input())
keys_pushes = [int(x) for x in input().split()]

for key in keys_pushes:
    keys_durability[key - 1] -= 1

for key in keys_durability:
    print("YES" if key < 0 else "NO")
