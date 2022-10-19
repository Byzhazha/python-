s = "hello,python"
s1 = s[:5]
s2 = s[6:]
s3 = "!"
new = s1 + s3 + s2
print(new)
print(id(s), id(s1), id(s2), id(s3), id(new))
