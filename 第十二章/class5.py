class Student:  # student 为类的名称（类名）由一个或多个单词组成，每个单词的首字母大写，其余小写
    native_pace = "密云"  # 直接写在类里的变量，称为类属性

    def __init__(self, name, age):
        self.name = name  # self.name称为实例属性，进行了一个赋值的操作，将局部变量的name的值赋给实体属性
        self.age = age

    # 实例方法
    def eat(self):
        print("学生在吃饭...")

    # 静态方法
    @staticmethod
    def method():
        print("我使用了staticmethod进行修饰，所以我是静态方法")

    # 类方法
    @classmethod
    def cm(cls):
        print("我是类方法，因为我使用了classmethod 进行修饰")


# 在类之外定义的称为函数，在类之内定义的称为方法
def drink():
    print("喝水")


# 类属性的使用方式 类中方法外的变量称为类属性，被该类的所有对象共享
stu1 = Student("张三", 20)
stu2 = Student("李四", 30)
print(stu1.native_pace)
print(stu2.native_pace)

print("-------------类方法的使用---------------")
Student.cm()
Student.method()
