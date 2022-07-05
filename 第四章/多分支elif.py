""""多分支结构 多选一执行 """
#90--100 A 80--89 B   70--79 C 60--69 D  0--59 D
while(1):
    score=int(input("请输入你的成绩:"))
    if 90<=score<=100:
        print("你还挺牛逼")
    elif 80<=score<=89:
        print("你真牛逼")
    elif 70<=score<=79:
        print("你不太行")
    elif 60<=score<=69:
        print("谢谢我吧你就")
    elif 0<=score<=59:
        print("滚蛋")