items = ["Fruits", "Books", "others"]
prices = [96, 78, 85]
d = {item.upper(): price for item, price in zip(items, prices)}  # upper 为转换成大写
print(d)
