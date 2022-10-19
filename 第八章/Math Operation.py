# 集合的数学操作
# 1.交集
s1 = {10, 20, 30, 40}
s2 = {20, 30, 40, 50, 60}
print(s1.intersection(s2))
print(s1 & s2)  # 与intersection等价

# 2.并集操作
print(s1.union(s2))
print(s1 | s2)

# 3.差集操作
print(s1.difference(s2))  # s1减去s1与s2的交集
print(s1 - s2)

# 4. 对称差集
print(s1.symmetric_difference(s2))
print(s1 ^ s2)  # 并集减去交集
