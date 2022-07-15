# 第一种办法  sort函数
list1 = [20, 40, 10, 98, 54]
print("排序前的列表：", list1, id(list1))
list1.sort()                     # 开始排序，调用列表对象的sort方法，升序排列
print("排序后：", list1, id(list1))          #     不产生新的列表
# 通过指定关键字参数，将列表中的元素进行降序排序
list1.sort(reverse=True)                    #  reverse     颠倒
print(list1)
# 第二种方法 sorted函数
print("-----------使用内置函数sorted（）对列表进行排序，将产生一个新的列表对象---------------")
list1 = [20, 40, 10, 98, 54]
print("原列表", list1)
# 开始排序
new_list = sorted(list1)
print(list1)
print(new_list)
# 指定关键字参数，实现列表元素的降序排列
desc_list = sorted(list1, reverse=True)
print("降序：", desc_list)
