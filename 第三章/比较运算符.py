a,b=10,20
print("a大于b吗？",a>b)#比较运算符得到的是True和False
#比较对象的标识使用 is
a=10
b=10
print(a==b)
print(a is b)#True 说明 a与b的地址相等
#以下代码没学过
list1=[11,22,33,44]
list2=[11,22,33,44]
print(list1 is list2)
print(id(list1),id(list2))        #id不同