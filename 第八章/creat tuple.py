"""元组的创建方式"""
""""1.使用（）"""
a = ("python", "world", 98)        # ()可以不写  不过只包含一个元素时，必须要写（）和， t=(10),
print(a,type(a))

"""2.内置函数 tuple（）"""
t = tuple(("python", "world", 98))
print(t,type(t))
