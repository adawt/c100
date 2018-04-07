"""
字符串排序
"""
strings = []
for _ in range(3):
    a = input('input:')
    strings.append(a)
strings.sort()

for a in strings:
    print(a, end='')
print('\n')

