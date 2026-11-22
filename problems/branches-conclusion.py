# https://coderun.yandex.ru/problem/branches-conclusion

import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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

result = []
stack = [root] if root is not None else []

while stack:
    node = stack.pop()

    has_left = node.left is not None
    has_right = node.right is not None

    if has_left != has_right:
        result.append(node.value)

    if node.left is not None:
        stack.append(node.left)
    if node.right is not None:
        stack.append(node.right)

for value in sorted(result):
    print(value)
