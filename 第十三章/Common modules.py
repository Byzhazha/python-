import sys            # 与python解释器及其环境操作相关的库
import time
import urllib.request   # 用于读取来自网上（服务器）的数据
import math
print(sys.getsizeof(24))
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))
print(time.time())
print(time.localtime())
print(urllib.request.urlopen('http://www.baidu.com').read())
