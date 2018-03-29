"""
【程序26】 
题目：利用递归方法求5!。
1.程序分析：递归公式：fn=fn_1*4!
2.程序源代码：
"""


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(5))