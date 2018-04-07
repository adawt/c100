"""
有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出 圈子，问最后留下的是原来排在第几号
"""

n = 10

# person = list(range(1, n + 1))

# count = 0
# while len(person) > 1:
#     print(person)
#
#     need_remove = []
#     for item in person:
#         count += 1
#         if count == 3:
#             need_remove.append(item)
#             count = 0
#
#     for item in need_remove:
#         person.remove(item)

# count = 0
# while len(person) > 1:
#     print(person)
#     for item in person[:]:
#         count += 1
#         if count == 3:
#             person.remove(item)
#             count = 0
#
# print(person[0])




count = 0
person = list(range(1, n + 1))
while len(person) > 1:
    for i in person[:]:
        count += 1
        if count == 3:
            person.remove(i)
            count = 0
print(person[0])






















