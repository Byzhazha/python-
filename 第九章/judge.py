s = "hello,python"
# 判断指定的字符串是不是合法的标识符
print("1.", s.isidentifier())  # False  有，
print("2.", "hello".isidentifier())
print("3.", "张三_".isidentifier())
print("4.", "张三_123".isidentifier())

# 判断指定的字符串是不是全部由空白字符组成（回车、换行、水平制表符）
test = "       "
print(test.isspace())

# 是否全由字母组成
test = "abcdefghijklmnopqrstuvwxyz"
print(test.isalpha())

# 是否为十进制数字
test = "10111001101"
print(test.isdecimal())

# 数字
print(test.isnumeric())

# 字母和数字
test = "123abc"
print(test.isalnum())
