"""
【程序5】
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
1.程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，
　　　　　　然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
2.程序源代码：
"""

x = int(input('x:\n'))
y = int(input('y:\n'))
z = int(input('z:\n'))

if x > y:
    a = x
    b = y
    x = b
    y = a
if x > z:
    c = x
    d = z
    x = d
    z = c
if y > z:
    e = y
    f = z
    y = f
    z = e
print(x, y, z)


if x > y:
    x, y = y, x

if x > z:
    x, z = z, x

if y > z:
    y, z = z, y

print(x, y, z)
