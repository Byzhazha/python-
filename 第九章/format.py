# 格式化字符串
# 1.    %占位符
name = "张三"
age = 20
print("我叫%s，今年%d岁" %(name,age))

# 2.{}
print("我叫{0}，今年{1}岁".format(name,age))

# 3.f-string
print(f"我叫{name},今年{age}岁")
a="I"
b="Love"
c="American"
d=f"{a} {b} {c}"
print(d)

print("%10d" % 99)           # 10d表示10个宽度
print("%.3f" % 3.1415926)

print("{0:.3}".format(3.1415926))       # 三个数
print("{0:.3f}".format(3.1415926))      # 三位小数
print("{:10.3f}".format(3.1415926))      # 10d    三位小数