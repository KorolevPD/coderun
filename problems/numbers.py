# https://coderun.yandex.ru/problem/numbers

from collections import deque

start = input().strip()
target = input().strip()


def get_next(number):
    result = []
    if number[0] != '9':
        result.append(str(int(number[0]) + 1) + number[1:])
    if number[3] != '1':
        result.append(number[:3] + str(int(number[3]) - 1))
    result.append(number[-1] + number[:-1])
    result.append(number[1:] + number[0])
    return result


parent = {start: None}
queue = deque([start])

while queue:
    current = queue.popleft()
    if current == target:
        break
    for next_number in get_next(current):
        if next_number not in parent:
            parent[next_number] = current
            queue.append(next_number)

path = []
current = target
while current is not None:
    path.append(current)
    current = parent[current]

path.reverse()
print('\n'.join(path))
