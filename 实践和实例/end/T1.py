sum1 = 0
a = input("请输入数字为")
b = set(a)
print(b)
for i in b:
    sum1 += int(i)
print(f"输出的结果为{sum1}")
