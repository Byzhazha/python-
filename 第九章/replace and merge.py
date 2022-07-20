# 替换
s = "hello,python"
print(s.replace("python","Java"))
s1 = "hello,python,python,python"
print(s1.replace("python","Java",2))

# 合并     (前提是列表和元组)
lst = ["hello","java","python"]
print("  ".join(lst))
tuple1 = ("hello","java","python")
print(",".join(tuple1))

print("*".join("java"))