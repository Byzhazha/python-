s = "hello,python"
# 判断指定的字符串是不是合法的标识符
print("1.",s.isidentifier())       # False  有，
print("2.","hello".isidentifier())
print("3.","张三_".isidentifier())
print("4.","张三_123".isidentifier())

#