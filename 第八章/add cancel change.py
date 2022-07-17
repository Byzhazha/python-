"""集合的相关操作"""
# 判断
s = {20, 30, 40, 50, 60}
print(10 in s)
print(100 not in s)

# 添加
s.add(80)
print(s)
s.update({200, 400, 300})
print(s)
s.update([100,98,8])
s.update((78,64,56))
print(s)

# 删除
s.remove(100)
s.discard(78)
s.discard(5000)         # 即使没有指定元素 也不会报错
print(s)
s.pop()            # 随机删除  里面不能写参数
print(s)
s.clear()
print(s)            # 清空
