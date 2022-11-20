import time as t
import random as r
start = t.perf_counter()
right = 0
list1 = []
list2 = []
list3 = []
list4 = []
for i in range(1, 1000):
    dur = 120 - (t.perf_counter() - start)
    if dur <= 60:
        break
    b = r.randint(1, 100)
    a = r.randint(0, 100)
    A = r.randint(1, 5)
    list1.append(a)
    list2.append(b)
    list3.append(A)
    if A == 1:
        print('{}+{}='.format(a, b), end='')
        jg = a + b
    elif A == 2:
        print('{}-{}='.format(a, b), end='')
        jg = a - b
    elif A == 3:
        print('{}*{}='.format(a, b), end='')
        jg = a * b
    else:
        print('{}/{}='.format(a, b), end='')
        jg = a / b
    jg = round(jg)
    list4.append(jg)
    shur = int(input())
    if shur == jg:
        right = right + 1
    dur_1 = 60 - (t.perf_counter() - start)
    print('时间还剩{:.2f}秒'.format(dur_1))
rate = 100 * right / i
print('{}题一共对了{}道正确率为{:.2f}'.format(i, right, rate))
exe = 0
for j in range(i - 1):
    if list3[j] == 1:
        print('{}+{}={}'.format(list1[j], list2[j], list4[j]))
    elif list3[j] == 2:
        print('{}-{}={}'.format(list1[j], list2[j], list4[j]))
    elif list3[j] == 3:
        print('{}*{}={}'.format(list1[j], list2[j], list4[j]))
    else:
        print('{}/{}={}'.format(list1[j], list2[j], list4[j]))
    exe = exe + 1
