file = open("1.txt", "r")
print(file.read(2))  # 读取两个字符
file.close()

file = open("1.txt", "r")
print(file.readline())  # 只读1行
file.close()

file = open("1.txt", "r")
print(file.readlines())  # 生成列表
file.close()

file1 = open("3.txt", "a")
lst = ["java", "go", "c"]
file1.writelines(lst)
file1.close()

# 文件指针
file2 = open("1.txt", "r")
file2.seek(2)  # 2个字节 一个汉字占了两个字节
print(file2.read())
print(file2.tell())
file2.close()
