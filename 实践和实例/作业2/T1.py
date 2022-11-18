while True:
    n = int(input())
    s = "*"
    if n % 2 != 0:
        for i in range(1, n + 1, 2):
            s1 = s * i
            print(s1.center(n, " "))
    else:
        print("请输入奇数")

