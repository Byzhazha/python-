class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 年龄不希望在在类的外部使用，所以加了两个__

    def show(self):
        print(self.name, self.__age)


stu = Student("张三", 20)
stu.show()
print(stu.name)
# print(stu.__age)           # AttributeError: 'Student' object has no attribute '__age'
print(dir(stu))
print(stu._Student__age)
