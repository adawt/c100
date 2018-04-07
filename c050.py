"""
编写input()和output()函数输入，输出5个学生的数据记录
"""


class Student:
    name = ''
    age = 0
    score = 0

    def input(self):
        self.name = input('name:')
        self.age = int(input('age:'))
        self.score = int(input('score:'))

    def output(self):
        print("name:%s,age:%d.score:%d" % (self.name, self.age, self.score))


students = []
for _ in range(5):
    stu = Student()
    stu.input()
    students.append(stu)

for i in students:
    i.output()

print("\n")