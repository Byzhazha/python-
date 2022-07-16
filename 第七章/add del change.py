"""key的判断"""
abcd = {"张三": 100, "李四": 98, "王五":45}
print("张三" in abcd)
print("张三" not in abcd)

# 删除
del abcd["张三"]
# abcd.clear()                     # 清空字典
print(abcd)

# 添加
abcd["陈六"] = 98
print(abcd)

# 修改
abcd["李四"] = 86
print(abcd)
