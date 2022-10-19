import os

print(os.getcwd())  # 返回当前的工作目录

ist = os.listdir("../第十四章")  # 返回指定路径下的文件和目录信息
print(ist)

# os.mkdir("new_dir")       # 一级目录
# os.makedirs("A/B/C")      # 创建多级目录
# os.rmdir("newdir")
# os.removedirs("A/B/C")

os.chdir(r"D:\python编程\第十四章")  # 改为别的目录
print(os.getcwd())
