list1 = ["hello", "world", 98, "hello"]
print(list1.index("hello"))  # 结果只为0 因为如查列表中存在n个相同元素，只返回第一个元素的索引
# print(list1.index("hello",1,3))     # 不包括3
# ValueError: 'hello' is not in list
#   指定范围内查找索引
print(list1.index("hello", 1, 4))
