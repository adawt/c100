"""'
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时
　　　共有5个数相加)，几个数相加有键盘控制。
1.程序分析：关键是计算出每一项的值。
2.程序源代码：
"""
# a = int(input('a = \n'))
# n = int(input('n = \n'))
# Tn = 0
# Sn = 0
# for i in range(n):
#     Tn = Tn + a
#     a = a * 10
#     Sn = Sn + Tn
# print(Sn)

a = input('a = ')
n = int(input('n = '))
print(sum([int(a * i) for i in range(1, n + 1)]))   # 列表推导式


# my_list = []
# for i in range(1, n + 1):
#     my_list.append(int(a * i))
# sum(my_list)
