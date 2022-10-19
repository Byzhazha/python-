file = open("1.txt", "r")
print(file.read())
file.close()  # 文件需是ansi格式  也就是GBK

file = open("2.txt", "w")
file.write("python")
file.close()

file = open("2.txt", "a")
file.write("p5415656")
file.close()

src_file = open("1.jpg", "rb")  # 二进制文件
target_file = open("copy1.jpg", "wb")
print(target_file.write(src_file.read()))
target_file.close()
src_file.close()

file1 = open('2.txt', 'a+')  # 如果文件不存在就创建，如果存在，就在内容后面继续追加
print('hello world', file=file1)
file1.close()  # 以读写的方式打开文件，不能单独使用，需要与其他模式一起使用  例如 a+
