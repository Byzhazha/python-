# 末尾添加一个元素
list1 = [10, 20, 30]
print("添加之前：", list1, id(list1))
list1.append(100)
print("添加后：", list1, id(list1))
list2 = ["hello", "world"]
# list1.append(list2)
print(list1)                 # 将list2作为一个元素加给list1
list1.extend(list2)           # 分别 将两个元素添加到末尾
print(list1)

