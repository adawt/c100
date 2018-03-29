"""
【程序24】 
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
1.程序分析：请抓住分子与分母的变化规律。 
2.程序源代码：
"""
x = 2
Sn = 0
for y in range(1, 21):
    x = x + y - 1
    Sn = Sn + x/y
print(Sn)