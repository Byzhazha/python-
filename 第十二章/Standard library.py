from random import randint
from random import choice

print(randint(1, 60))
players = [1, 2, 3, 4, 5, 6, "sd"]  # 它将一个列表或元组作为参数，并随机返回其中的一个元素
first_up = choice(players)
print(first_up)
