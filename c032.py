"""
Press any key to change color, do you want to try it. Please

hurry up!
"""
for atrr in [0, 1, 4, 5, 7]:
    print("attribute %d ------------------------------" % atrr)
    for fore in [30, 31, 32, 33, 34, 35, 36, 37]:
        for back in [40, 41, 42, 43, 44, 45, 46, 47]:
            color = "\033[%d;%d;%dm" % (atrr,fore,back)
            print("%s %d-%d-%d\033[0m" % (color,atrr,fore,back),end='')
        print()
