"""
对10个数进行排序


程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个

元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。 　　　
"""

numbers = input('输入n个整数(split by ,): ')

numbers = [int(i) for i in numbers.split(',')]
print('before sort', numbers)
numbers.sort()
print('after sort', numbers)
