import os
path = os.getcwd()
lst_files = os.walk(path)
for dirpath, dirname, filename in lst_files:
    # print(dirpath)                 # 目录
    # print(dirname)                 # 子目录
    # print(filename)                # 文件名
    # print("------------------")

    for dir in dirname:
        print(os.path.join(dirpath, dir))

    for file in filename:
        print(os.path.join(dirpath,file))

    print("------------------")

