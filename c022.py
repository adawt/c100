"""
【程序22】
题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定
　　　比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出
　　　三队赛手的名单。
1.程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，
　　　　　　则表明此数不是素数，反之是素数。 　　　　　　
2.程序源代码：
"""

for play1 in 'abc':
    for play2 in 'xyz':
        if (play1 == 'a' and play2 != 'x') and (play1 == 'c' and play2 not in 'xz'):
                print('%d----%d' % (play1, play2))
