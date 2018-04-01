"""
求一个3*3矩阵对角线元素之和

程序分析：利用双重for循环控制输入二维数组，再将a累加后输出。
"""
numbers = input('输入 matrix(rows split by ";", columns split by ","): ')
a = [[int(col) for col in row.split(',')] for row in numbers.split(';')]
print(a)

count1 = sum(a[i][i] for i in range(len(a)))
print(count1)
count2 = sum(a[j][len(a)-1-j]for j in range(len(a)))
print(count2)
