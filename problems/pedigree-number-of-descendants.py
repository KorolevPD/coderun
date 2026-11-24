# https://coderun.yandex.ru/problem/pedigree-number-of-descendants

import sys

data = sys.stdin.read().split()
n = int(data[0])

children = {}
names = set()
with_parent = set()

index = 1
for _ in range(n - 1):
    child = data[index]
    parent = data[index + 1]
    index += 2

    children.setdefault(parent, []).append(child)
    names.add(child)
    names.add(parent)
    with_parent.add(child)

if n > 1:
    root = next(iter(names - with_parent))

    order = []
    stack = [root]

    while stack:
        person = stack.pop()
        order.append(person)
        for child in children.get(person, []):
            stack.append(child)

    descendants = {}

    for person in reversed(order):
        total = 0
        for child in children.get(person, []):
            total += 1 + descendants[child]
        descendants[person] = total

    for person in sorted(names):
        print(person, descendants[person])
