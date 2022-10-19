a = "天涯共此时"
print(a.encode(encoding="GBK"))  # 在gbk的编码格式上，一个中文占两个字节
print(a.encode(encoding="UTF-8"))  # 在utf-8的编码格式上，占三个字节

# 解码
# byte 代表就是一个二进制数据（字节类型的数据）
byte = a.encode(encoding="GBK")
print(byte.decode(encoding="GBK"))
byte = a.encode(encoding="UTF-8")
print(byte.decode(encoding="UTF-8"))
