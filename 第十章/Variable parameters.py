def fun(*args):  # 个数可变的位置参数
    print(args)  # 定义函数时，可能无法事先确定传递的位置实参的个数时，使用可变的位置   结果为一个元组


fun(10)
fun(10, 30)
fun(30, 405, 50)


def fun1(**arge):  # 个数可变的关键字形参
    print(arge)  # 定义函数时，可能无法事先确定传递的关键字实参的个数时，使用可变的关键字形参 结果为字典


fun1(a=10)
fun1(a=10, b=20, c=30)

print("java", "c", "python")  # def print(self, *args, sep=' ', end='\n', file=None): # known special case of print


#              所以print 函数是个数可变的位置参数


def fun2(*args1, **args2):
    pass

# def fun3(**args2,*asg12):
#     pass
#  在一个函数的定义过程中，既有个数可变的关键字形参，也有个数可变的位置形参，要求，个数可变的位置形参，放在个数可变的关键字之前
