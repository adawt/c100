"""
有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数

组中。1,4,6,9,13,16,19,28,40,100
"""
N = [1, 4, 6, 9, 13, 16, 19, 28, 40, 100]
a = int(input('a = :'))
N.append(a)
# for i in range(9,-1,-1):
#     if N[i] > N[i + 1]:
#         N[i], N[i+1] = N[i+1], N[i]
# print(N)
N.sort()
print(N)

