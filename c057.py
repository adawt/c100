"""
找到年龄最大的人，并输出。
"""
persons = {"a": 16, "b": 18, "c": 19, "d": 20}
current = ""
for key in persons:
    if current == "":
        current = key
    else:
        if persons[current] < persons[key]:
            current = key
print("%s: %d" % (current, persons[current]))
