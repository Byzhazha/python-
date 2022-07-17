# s1 = {10,20,30,40}
# s2 = {40,30,20,10}
# print(s1==s2)  # 两个集合相等 元素相等即为相等
"""一个集合是否为另一个集合的子集"""
s1={10,20,30,40,50,60}
s2={10,20,30,40}
s3={10,20,90}
print(s2.issubset(s1))
print(s3.issubset(s2))
"""一个集合是否为一个集合的超集"""
print(s1.issuperset(s2))
print(s1.issuperset(s3))

"""两个集合是否含有交集"""
print(s2.isdisjoint(s3))     # False  有交集
s4={100,200,300,400}
print(s2.isdisjoint(s4))     # True  没有交集