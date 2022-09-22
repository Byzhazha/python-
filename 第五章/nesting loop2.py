# 输出九九乘法表
for row in range(1, 10):
    for column in range(1, row + 1):
        print(row, "*", column, "=", row * column, end="  ")
    print()
