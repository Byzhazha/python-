#  字符串驻留机制
a='python'
b="python"
c="""python"""
print(a,id(a))
print(b,id(b))
print(c,id(c))        #  对相同的字符串只保留一份拷贝，后续创建相同字符串时，不会开辟新空间，而是把该字符串的地址赋值给新创建的变量
