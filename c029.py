"""
【程序29】 
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
1. 程序分析：学会分解出每一位数，如下解释：(这里是一种简单的算法，师专数002班赵鑫提供) 
2.程序源代码：
"""
x = int(input('input number:\n'))
a = int(x/10000)
b = int(x/1000 % 10)
c = int(x/100 % 10)
d = int(x/10 % 10)
e = int(x % 10)
if a != 0:
    print('5')
    print(e, d, c, b, a)
elif b != 0:
    print('4')
    print(e, d, c, b)
elif c != 0:
    print('3')
    print(e, d, c)
elif d != 0:
    print('2')
    print(e, d)
else:
    print('1')
    print(e)
