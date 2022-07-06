# 从键盘录入密码 最多录入3次 如果正确就结束循环
for _ in range(3):
    password = input("请输入密码:")
    if password == "8888":
        print("密码正确")
        break
    else:
        print("密码不正确")