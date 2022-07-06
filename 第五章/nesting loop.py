""""输出一个三行四列的矩形"""
for row in range(1, 4):
    for column in range(1, 5):
        print("*", end="\t")         # print默认是打印一行，结尾加换行。end=' '意思是末尾不换行，加空格
    print()                # 什么都不给 相当于换行
