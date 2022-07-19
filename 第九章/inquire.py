# 字符串的查询操作
s = "hello,hello"
print(s.index("lo"))
print(s.find("lo"))
print(s.rindex("lo"))
print(s.rfind("lo"))
#-11 -10 -9 -8 -7 -6 -5 -4 -3 -2  -1      逆向索引
# h   e   l  l  o  ,  h  e  l   l  o
# 0   1   2  3  4  5  6  7  8   9  10      正向索引
print(s.rfind("k"))
print(s.find("k"))         # find 和 rfind 在查找的字符串不存在时，则返回-1
# 而index和 rindex 则会抛出value error
