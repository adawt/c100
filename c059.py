"""
海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。第二只猴子把剩下的
桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个
"""

monkey_num = 5
#
#
# for guess in range(10000):
#     total = guess
#     ok = True
#
#     print('guess', guess)
#
#     for monkey in range(monkey_num - 1):
#         total = ((5 * total) + 1)
#         if total % 4 != 0:
#             ok = False
#             break
#         total = total // 4
#
#     if ok:
#         print((5 * total) + 1)
#         break

a = 4**(monkey_num-1)
b = 5**monkey_num

for i in range(10000):
    if a * (i + 4) % b == 0:
        print(i)
        break
