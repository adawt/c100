"""
请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，

则继续判断第二个字母。
"""
n1 = input('input first letter =:')
if n1 == 'T':
    n2 = input('input second letter:')
    if n2 == 'u':
        print('Tuesday 2')
    elif n2 == 'h':
        print('Thursday 4')
    else:
        print('error')
elif n1 == 'S':
    n2 = input('input second letter:')
    if n2 == 'u':
        print('Sunday 7')
    elif n2 == 'a':
        print('Saturday 6')
    else:
        print('error')
elif n1 == 'M':
        print('Monday 1')
elif n1 == 'W':
        print('Wednesday 3')
elif n1 == 'F':
        print('Friday 5')
else:
    print('error')
