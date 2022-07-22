def fun(*args):          # 个数可变的位置参数
    print(args)          # 定义函数时，可能无法事先确定传递的位置实参的个数时，使用可变的位置   结果为一个元组


fun(10)
fun(10,30)
fun(30,405,50)

def fun1(**arge):         # 个数可变的关键字形参
    print(arge)           # 定义函数时，可能无法事先确定传递的关键字实参的个数时，使用可变的关键字形参 结果为字典

fun1(a=10)
fun1(a=10,b=20,c=30)

print("java", "c","python")       # def print(self, *args, sep=' ', end='\n', file=None): # known special case of print
#              所以print 函数是个数可变的位置参数