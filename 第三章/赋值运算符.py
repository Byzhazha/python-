a=b=c=20
print(a,id(a))
print(b,id(b))
print(c,id(c)) #三个id都一样 也就是地址一样 这和c语言有区别    再次运行 地址会变 和c语言一样
d,e,f=20,30,40
print(d,e,f)
print("------------交换两个变量的值---------------")
a,b=10,20
print("交换前",a,b)
a,b=b,a
print("后",a,b)

