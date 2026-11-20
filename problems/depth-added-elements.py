# https://coderun.yandex.ru/problem/depth-added-elements

import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


numbers = [int(x) for x in sys.stdin.buffer.read().split()]

root = None
depths = []

for value in numbers:
    if value == 0:
        break

    if root is None:
        root = Node(value)
        depths.append(1)
        continue

    current = root
    depth = 1

    while True:
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
                depth += 1
                depths.append(depth)
                break
            current = current.left
            depth += 1
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
                depth += 1
                depths.append(depth)
                break
            current = current.right
            depth += 1
        else:
            break

print(*depths)
