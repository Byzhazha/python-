class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 创建c类对象
x = C("Jack", 18)  # x是C类型的一个实例化对象
print(x.__dict__)  # 实例对象的属性字典
print(C.__dict__)
print("---------------")
print(x.__class__)  # <class '__main__.C'> 输出了对象所属的类
print(C.__bases__)  # C类的父类类元素
print(C.__base__)
print(C.mro())  # 类的层次结构
print(A.__subclasses__())  # 子类
