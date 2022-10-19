list1 = [10, 20, 30, 40, 50, 60, 30]
list1.remove(30)
print(list1)  # 也是只删除重复的第一个元素

# pop 根据索引移除元素
list1.pop(1)
print(list1)
list1.pop()  # 如果不指定元素 则删除最后一个
print(list1)
# # 切片 删除 至少一个元素 将产生新的一个列表对象
# list2 = list1[1:3]
# print("原列表:", list1)
# print("切片后：", list2)
# 不产生新的列表对象  而是删除原列表中的内容
list1[1:3] = []
print(list1)
print(list1.count(10))  # 计数器
"""清除列表中的所有元素"""
list1.clear()
print(list1)
del list1
