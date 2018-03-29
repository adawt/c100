"""
【程序12】
题目：判断101-200之间有多少个素数，并输出所有素数。
1.程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，
　　　　　　则表明此数不是素数，反之是素数。 　　　　　　
2.程序源代码：
"""
count = 0
for i in range(101, 201):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        count += 1
        print(i)
print('101到200之间有%d个素数' % count)
