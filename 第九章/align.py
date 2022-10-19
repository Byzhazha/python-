s = "hello,python"
"""居中对齐"""
print(s.center(20, "*"))
"""左对齐"""
print(s.ljust(20, "*"))
print(s.ljust(10))  # 小于实际长度，则返回原字符
print(s.ljust(20))
"""右对齐"""
print(s.rjust(20, "*"))
print(s.rjust(10))
print(s.rjust(20))

# 右对齐 使用0填充
print(s.zfill(20))
