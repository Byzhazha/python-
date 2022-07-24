class Student:                # student 为类的名称（类名）由一个或多个单词组成，每个单词的首字母大写，其余小写
    pass

# python 中一切皆对象 student是对象吗？内存有开空间吗？
print(id(Student))            #   1879890884992
print(type(Student))          # <class 'type'>
print(Student)                # <class '__main__.Student'>
