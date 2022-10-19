list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# start=1 stop=6 step=1
print(list1[1:6:1])  # 左闭右开  不包括6 默认步长为1 从0开始 到最后一个结束
print("原列表", id(list1))
list2 = list1[1:6:1]  # 新列表
print("切的片段", id(list2))
print("---------step为负数的情况下---------")
print(list1[::1])  # 逆序输出
print(list1[6:0:-2])
