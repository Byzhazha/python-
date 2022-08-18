for love in "python":     # love为变量  依次取值赋给变量
    print(love)

# range（）产生一个整数序列   也是一个可迭代对象
for item in range(10):
    print(item)
# 如果在循环体中不需要使用到自定义变量，可将变量写为“_”
for _ in range(5):
    print("人生苦短，我用c语言")
# 用for in写 1到100之间的偶数和
num=0
sum1=0
for num in range(0, 101, 2):
    sum1=sum1+num
print(sum1)
# 水仙花数 例如 153=3*3*3+5*5*5+1*1*1 水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身
# 输出100到999的 水仙花数
cou = 0    # 计数器
for num2 in range(100, 1000):
    ge = num2 % 10
    shi = num2 // 10 % 10  # //整除
    bai = num2 // 100
    # print(ge, shi, bai)

    if ge**3+shi**3+bai**3 == num2:
        cou = cou + 1
        print(num2)
print(cou)
