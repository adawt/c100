"""
将一个数组逆序输出。

程序分析：用第一个与最后一个交换。

"""

numbers = input('输入n个整数(split by ,): ')

numbers = [int(i) for i in numbers.split(',')]
n = int(len(numbers))
for i in range(0, n//2):
    numbers[i], numbers[n-1-i] = numbers[n-1-i], numbers[i]
print(numbers)
