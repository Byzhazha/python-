def calc(a,b):
    sum1=a+b
    return sum1


result=calc(10,20)                   # result=calc(b=100,a=20)
print(result)                        # print(result)          此方法也可行

# 在函数的调用过程中，进行参数的传递
"""如果是不可变对象，在函数体的修改不会影响实参的值
   如果是可变对象，  在函数体的修改会影响实参的值  append（）
"""

