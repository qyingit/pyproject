# 包也是一个模块
#模块的代码过多时使用包
#普通的模块是py文件  包是一个文件夹
#__init__.py文件，这个文件包含包中的主要内容
#import test_mo as te
from test_mo import a,b
print(b.d)

#__pycache__模块的缓存文件
#py 代码在执行前，需要被解析器先转为机器码，然后在执行
#所以一在使用模块包的时候，模块先转为机器码再执行
#为了提高效率先编译到缓存文件中，到时候运行的时候直接调用