class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + "在吃饭")


stu1 = Student("李佳阳", 19)
stu2 = Student("张三", 19)
print(id(stu1))
print(id(stu2))

print("----------为stu2动态绑定性别属性-------------")
stu2.gender = "女"
print(stu2.name, stu2.age, stu2.gender)

print("--------------------")
stu2.eat()
stu1.eat()


def show():
    print("定义在类之外的，称为函数")


stu1.show = show  # 动态绑定方法
stu1.show()
