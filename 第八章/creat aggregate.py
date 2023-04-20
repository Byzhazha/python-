"""第一种创建方式 {}"""
s = {2, 3, 4, 5, 5, 6, 7, 7}
print(s, type(s))  # 集合中的元素不允许重复
"""第二种创建方式"""
s1 = set(range(6))
print(s1, type(s1))
s2 = {1, 2, 3, 4, 5, 6}
print(s2, type(s2))
s3 = set((1, 2, 4, 4, 5, 65))
print(s3)  # 无序
s4 = set("python")
print(s4, type(s4))
