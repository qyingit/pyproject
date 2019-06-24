#开箱即用  py提供了一个标准库可以直接使用
#标准库随python的安装即可使用

#sys模块 提供一些变量和函数，是我们可以获取到python解析器的信息
 #通过函数来操作python解析器

import sys

print(sys.argv)

#获取返回的模块 字典的格式
print(sys.modules)

# ppprint模块 可以对打印的数据简单的格式化
import pprint
pprint.pprint(sys.modules)

#获取路径，列表中保存的是模块搜索的路径
pprint.pprint(sys.path)

#python的运行平台
print(sys.platform)

#sys.exit  程序退出
#sys.exit("程序异常")
print("hello")

#os 可以对操作系统进行访问
import os
#获取系统的环境变量
pprint.pprint(os.environ['path'])

os.system("dir")

