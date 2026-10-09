# https://coderun.yandex.ru/problem/triangle

nums = sorted(int(input()) for _ in range(3))
print('YES' if nums[2] < nums[0] + nums[1] else 'NO')
