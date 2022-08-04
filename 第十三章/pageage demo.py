import pageage1.modul1 as ma
import pageage1.modul2 as f
print(ma.a)
print(f.b)
# 导入带有包的模块时注意事项
import pageage1
import calc
# 使用import 方式进行导入时，只能跟包名或模块名

from pageage1 import modul1
from pageage1.modul1 import a
# 使用from...import可以导入包、模块、函数、变量
