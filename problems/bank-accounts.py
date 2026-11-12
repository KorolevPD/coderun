# https://coderun.yandex.ru/problem/bank-accounts

import sys

accounts = {}

for line in sys.stdin:
    parts = line.split()
    if not parts:
        continue

    operation = parts[0]

    if operation == 'DEPOSIT':
        name = parts[1]
        amount = int(parts[2])
        accounts[name] = accounts.get(name, 0) + amount

    elif operation == 'WITHDRAW':
        name = parts[1]
        amount = int(parts[2])
        accounts[name] = accounts.get(name, 0) - amount

    elif operation == 'BALANCE':
        name = parts[1]
        if name in accounts:
            print(accounts[name])
        else:
            print('ERROR')

    elif operation == 'TRANSFER':
        sender = parts[1]
        receiver = parts[2]
        amount = int(parts[3])
        accounts[sender] = accounts.get(sender, 0) - amount
        accounts[receiver] = accounts.get(receiver, 0) + amount

    elif operation == 'INCOME':
        percent = int(parts[1])
        for name in accounts:
            if accounts[name] > 0:
                accounts[name] += accounts[name] * percent // 100
