# 用于结束当前循环 进入下一次循环 通常与if一起使用
# 要求输出1--50之间5的倍数
for num in range(1,51):
    if num % 5 != 0:
        continue
    print(num)