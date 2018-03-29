"""
【程序27】 
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
1.程序分析：
2.程序源代码：
"""
string = input("input string:\n")


def f(x):
    if x == -1:
        return ""
    else:
        return string[x] + f(x-1)


print(f(len(string) - 1))