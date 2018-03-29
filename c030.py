"""
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。　　　
1.程序分析：同29例
2.程序源代码：
"""
x = int(input('input number:\n'))
a = int(x/10000)
b = int(x/1000 % 10)
c = int(x/100 % 10)
d = int(x/10 % 10)
e = int(x % 10)
if a == e and b == d:
    print('1')
else:
    print('0')


