"""
【程序9】
题目：要求输出国际象棋棋盘。
1.程序分析：用i控制行，j来控制列，根据i+j的和的变化来控制输出黑方格，还是白方格。
2.程序源代码：
"""
for i in range(1, 9):
    for j in range(1, 9):
        if (i + j) % 2 == 0:
            print('1 ', end='')
        else:
            print('0 ', end='')
    print('')
