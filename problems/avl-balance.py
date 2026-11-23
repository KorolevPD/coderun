# https://coderun.yandex.ru/problem/avl-balance

import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


numbers = [int(x) for x in sys.stdin.buffer.read().split()]

root = None

for value in numbers:
    if value == 0:
        break

    if root is None:
        root = Node(value)
        continue

    current = root

    while True:
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
                break
            current = current.left
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
                break
            current = current.right
        else:
            break

balanced = True

if root is not None:
    stack = [(root, False)]

    while stack:
        node, processed = stack.pop()

        if processed:
            left_height = node.left.height if node.left is not None else 0
            right_height = node.right.height if node.right is not None else 0

            if abs(left_height - right_height) > 1:
                balanced = False
                break

            node.height = 1 + max(left_height, right_height)
        else:
            stack.append((node, True))
            if node.left is not None:
                stack.append((node.left, False))
            if node.right is not None:
                stack.append((node.right, False))

print('YES' if balanced else 'NO')
