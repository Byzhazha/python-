abcd = {"张三": 100, "李四": 98, "王五": 45}
keys = abcd.keys()
print(keys, type(keys))
print(list(keys))  # 将所有的key组成的视图转成列表

# 获取所有的值
values = abcd.values()
print(values, type(values))

# 获取所有键值对
items = abcd.items()
print(items)
print(list(items))  # 转换之后的列表元素是由元组组成   后续会讲到
