print('hello\nworld')
print('hello\tworld')
print('helloooo\tworld')  # 制表符 4个位
print('hello\rworld')  # world对hello进行了覆盖
print('hello\bworld')  # 退一个格
print('http://www.baidu.com')
print('老师说：\'大家好\'')
# 原字符：不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r或R
print(r'hello\nworld')
# 最后一个字符不能是反斜杠
print('hello world\\')
