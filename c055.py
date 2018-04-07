"""
编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
"""
num = int(input('输入:'))
s = 0

for i in range(1, num + 1):
    current = 0
    if num % 2 == 0:
        if i % 2 == 0:
            current = 1/i
    else:
        if i % 2 != 0:
            current = 1/i
    s += current
print(s, '\n')
