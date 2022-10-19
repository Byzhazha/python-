# rand的三种创建方式
# 第一种，只有一个参数，小括号只给了一个数
r = range(10)  # 默认从0开始，相差1(步长)
print(r)
print(list(r))  # 查看range对象中的整数序列  list是列表的意思
# 第二种 两个参数 开始和结束
r = range(1, 10)
print(list(r))
# 第三种 三个参数 开始 结束 步长
r = range(1, 10, 2)
print(list(r))
print(range(1, 20, 2))
""""判断指定的整数 在序列中是否存在 in not in"""
print(10 in r)
