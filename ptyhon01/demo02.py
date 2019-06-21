# boolean
a = True
a = False
print(f"a={a}")
#布尔值属于整型 True为1 False为0
#None 空值 专门表示不存在
a= None

# 类型检查
a= 123
b = '123'
# print("a=",a)
# print("b=",a)
# 类型检查。可以检查只能值变量的类型
# c = type(123)
# print(c)
# c = type(123)
# print(c )

print(type(1))
print(type(1.5))
print(type("hello"))
print(type(True))
print(type(None))

#python 是面向对象的语言
#程序运行中，所有的数据在内存中在运行的
#对象就是内存中专门存储指定数据的一块区域
# 对象实际上就是一个容器，专门用来存储数据
# 数值，字符串，布尔值，None就是对象

# 对象的结够 每个对象有三种数据
# id(标识)标识对象的唯一性,每个对象有唯一的id，通过id()函数查看对象id,由解析器生成，在cpython中,id就是内存地址吗，对象创建则id不会改变
print(id(213))
#type标识当前对象的所属类型
# 比如 ：int float
# 类型决定有哪些功能
#对象一旦创建则类型不能修改

# value
# 对象中的具体数据
# eg: str="ad"  id=1312  type = String value = "ad"
# 可变对象与不可变对象
# 不可变对象:str int  boolean 已经存在的对象



#变量与对象的关系
# a=123  内存专门的区域存储变量
# 变量 值  变量a 存123的地址值
# 变量中保存的对象,只有在重新赋值的时候才会改变
# 变量与变量之间是相互独立的

## 运算符与操作符
# 运算符可以对一个值或多个值进行运算或各种操作
# 算术运算  + - * /  字符串没有-与/
# 两个//表示整除
# 两个** 表示幂运算
a = 10 // 3
a = 2**3
# %取模运算
a =10 %6
print(a)
# 赋值运算
# 将等号右侧的值给左侧
# += -= *= /= **= //= %=
a = 25.0
a //=3
print(a)

# 关系运算符
# > < >= <= == !=  不同类型不能 比较
# 在python可以对字符串进行大于与小于的比较,比的是unicode，多个字符逐字比较
#相等与不等比较的是值
result = 'a' > 'b'
print(result)
# is isnot 比较两个睢县是否是同一个对象
result = (213)is(123)
print(result)
# 逻辑运算符
# 做一些逻辑判断
# not 可以对符号进行非运算，会进行去翻操作，false变为true
# 对于非布尔值，会转为布尔值，在取反
result ='213'
print(not result)
# and
# 可以对符号两侧数据进行与运算
# python中的与运算是短路与
result = True and print(result)
result = False and print(result)
# or
# 进行或运算 python中是短路或
result = True or False
print(result)

print(3 or 0)
print(3 and 0)

# 条件运算符(三元运算符)
# 语法: 语句1 if 条件表达式  else 语句2
print("hello") if False else print("nonono")

a = 2 if True else 3
print(a)

a = 10
b = 20
c = 30
k = a if a>b else b
k = k if k>c else c
print(k)
