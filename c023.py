"""
【程序23】 
题目：打印出如下图案（菱形）

   *
  ***
 *****
*******
 *****
  ***
   *
1.程序分析：先把图形分成两部分来看待，前四行一个规律，后三行一个规律，利用双重
　　　　　　for循环，第一层控制行，第二层控制列。 
2.程序源代码： 
"""
# for i in range(1, 9, 2):
#     print(' '*((7-i)//2), end='')
#     print('*'*i)
# for j in range(5, -1, -2):
#     print(' ' * ((7 - j) // 2), end='')
#     print('*'*j)
n = int(input('n =:\n'))
if n % 2 != 0:
    for i in range(1, n+2, 2):
        print(' '*((n-i)//2), end='')
        print('*'*i)
    for j in range(n-2, -1, -2):
        print(' ' * ((n - j) // 2), end='')
        print('*'*j)
else:
    print("error")

