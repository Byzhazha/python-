import jieba
txt = open("沉默的羔羊.txt", encoding="utf-8").read()
words = jieba.lcut(txt)  # lcut 函数是精确分割模式
counts = {}
for word in words:
    if len(word) < 2:  # 判断小于2个字的直接跳过
        continue
    else:  # 大于2个字的进行计算出现次数
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
print(items[0])
print(items[0][0])
