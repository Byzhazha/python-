a = 0
while a < 3:
    password = input("请输入密码")
    if password == "8888":
        print("密码正确")
        break
    else:
        print("不正确")
    a += 1
else:
    print("对不起，机会用尽，估计不是您的号")
