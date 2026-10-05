# https://coderun.yandex.ru/problem/polyglots

with open('input.txt', 'r', encoding='utf-8') as fin:
    lines = [line.strip() for line in fin if line.strip()]

n = int(lines[0])
idx = 1
unique_set = set()
common_set = None

for _ in range(n):
    m = int(lines[idx])
    idx += 1
    input_set = set(lines[idx:idx + m])
    idx += m

    if common_set is None:
        common_set = input_set
    else:
        common_set &= input_set

    unique_set |= input_set

common_set = common_set or set()

with open('output.txt', 'w', encoding='utf-8') as fout:
    fout.write(str(len(common_set)) + '\n')
    for lang in sorted(common_set):
        fout.write(lang + '\n')
    fout.write(str(len(unique_set)) + '\n')
    for lang in sorted(unique_set):
        fout.write(lang + '\n')
