"""
打印出杨辉三角（要求打印出10行）
"""
n = 10

last_line = [1]
for i in range(n):
    print(*last_line)

    new_line = [last_line[0]]

    for j in range(len(last_line) - 1):
        new_line.append(last_line[j] + last_line[j + 1])

    new_line.append(last_line[-1])

    last_line = new_line

