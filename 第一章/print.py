#写入文件夹
wk=open('D:/text.txt','a+')#如果文件不存在就创建，如果存在，就在内容后面继续追加
print('hello world',file=wk)
wk.close()