"""获取字典的元素"""
abcd = {"张三": 100, "李四": 98, "王五":45}
"""第一种方式    【】"""
print(abcd["张三"])
# print(abcd["456"])     KeyError: '456'
"""第二种方式 get函数"""
print(abcd.get("张三"))
print(abcd.get("456"))            # None
print(abcd.get("程鸿悦", 99))  # 99是在查找key所对的value不存在时，提供的一个默认值
