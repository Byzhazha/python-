#    判断奇偶数
def fun(num):
    odd = []    # 存放奇数
    even = []       # 偶数
    for i in num:
        if i % 2==0:
            odd.append(i)
        else:
            even.append(i)
    return odd,even


list1 = [10, 29, 34, 23, 44, 53, 55]
print(fun(list1))
