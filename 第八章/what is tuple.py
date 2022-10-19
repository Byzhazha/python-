"""可变序列 不可变序列"""
"""可变序列： 列表，字典"""
lis = [10, 20, 45]
print(id(lis))
lis.append(300)
print(id(lis))
# 不可变序列 字符串 元组 没有增删改操作
s = "hello"
print(id(s))
s = s + "world"
print(s, id(s))  # id 发生变化
