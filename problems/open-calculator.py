# https://coderun.yandex.ru/problem/open-calculator

keys = set(input().split())
nums = set(input())
print(len(nums.difference(keys)))
