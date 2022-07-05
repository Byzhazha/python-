ret=1
while(ret<10):
    print(ret)
    ret=ret+1
#计算0到4之间的累加和
a=0
sum=0
while a < 5:
    sum=a+sum
    a=a+1
print("和为：",sum)
#计算1到100之间的偶数
num=0
sum=0
while num <= 100:

    if num % 2 == 0:
        sum=sum+num
    num=num+1
print(sum)