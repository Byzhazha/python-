s = "hello world python"
lis = s.split()  # 返回列表格式
print(lis)
s1 = "hello|world|Python"
print(s1.split(sep="|"))
print(s1.split(sep="|", maxsplit=1))  # 只分割一段
# rsplit 原理同上 从右开始分割
