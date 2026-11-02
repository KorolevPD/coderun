# https://coderun.yandex.ru/problem/phone-numbers


def normalize(number):
    digits = ''.join(ch for ch in number if ch.isdigit())

    if len(digits) == 11 and digits[0] in '78':
        digits = digits[1:]

    if len(digits) == 7:
        digits = '495' + digits

    return digits


new_number = normalize(input().strip())

for _ in range(3):
    number = normalize(input().strip())
    print('YES' if number == new_number else 'NO')
