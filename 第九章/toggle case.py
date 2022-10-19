"""字符串中大小写转换的方法"""
s = "hello,python"
# 全部转换为大写
print(s.upper(), id(s.upper), id(s))  # 会产生一个新的字符串
# 全部转换为小写
small = s.lower()
print(small, id(s), id(small))
print(small == s)
print(small is s)
# 所有大写转为小写，所有小写转为大写 swapcase
s2 = "hello,Python"
print(s2.swapcase())

# 第一个字符大写，其余小写
print(s2.capitalize())

# 首字母大写 其余小写
print(s2.title())
