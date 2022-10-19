# squares = []
# for value in range(1, 11):
#     square = value**2
#     squares.append(square)
#
# print(squares)

squares = [value ** 2 for value in range(1, 11)]
print(squares)  # 列表解析

sum1 = [num for num in range(1, 21)]
print(sum1)
