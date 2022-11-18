txt = open("latex.log").read()
count = 0
dict1 = {}
for i in range(26):
    dict1[chr(ord('a')+i)] = 0
for line in txt:
    for word in line:
        dict1[word] = dict1.get(word, 0) + 1
print(len(txt))
for i in range(26):
    # if dict1[chr(ord('a')+i)] != 0:
    print(",{}:{}".format(chr(ord('a')+i), dict1[chr(ord('a')+i)]), end="")

