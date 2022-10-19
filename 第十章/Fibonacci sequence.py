def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        res = fib(n - 1) + fib(n - 2)
        return res


print(fib(6))
print("-----------------------")
for i in range(1, 7):
    print(fib(i))
