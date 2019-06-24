#python的模块化
#模块化,:将一个完整的程序编写为一个小的模块
#通过模块去组和程序
#不用模块会统一编写到一个程序
#模块化有点：
#  1.方便开发跟维护
#  2.模块可以复用


#模块化的应用
#python中的一个py文件就是模块 创建模块就是创建一个py文件

#在模块中引入外部模块
#1 import 模块名 (模块名是python的名字，注意不要py)
#  import test_module
#  import test_module
#可以引入同一个模块多次，但模块的实例只执行一次

import test_module as test
#print(test_module)
#as 给模块增加别名
#print(test)
#一般情况import写在程序的开头

#print(test.__name__)
#__name__ 为__main__，python中只有一个主模块。主模块直接通过python执行的模块
print(__name__)

# import m1
# #访问模块中的变量使用    模块名.属性值
# print(m1.a,m1.b)
#
# m1.test()
#
# person = m1.Person()
# print(person.name)

#可以只引入模块的部分内容
#语法 from 模块名 import 变量 ，变量
# from m1 import Person
#
# # from m1 import * 从模块中引入所有的内容 不推荐使用
# # 会倒置变量方法冲突
# p = Person()
# print(p.name)
#也可以引入的变量使用别名
#语法 from 模块名 import 变量 as 别名

# from m1 import test as new_test
# new_test()

#取消测试代码的测试
#当模块为主模块执行，如果为其它模块引入不需要执行
import m1

# import xxx
# import xxx as xxx