#异常和文件

##程序运行过程中，不可避免出现错误，比如使用更没有赋值的变量 ，不存在的索引

#程序一旦出现异常,程序会立即中止

#处理异常  python希望出现异常能够及时处理

#语法
#try :
#    代码块（可能出现错误的语句）
#except:
#    代码块(没出错要执行的语句)

# print("hello")
# try:
#     print(10/1)
# except:
#     print("error")
# else:
#     print("程序正常")
# print("你好")

#可以将出错的语句放入到try语句中，如果代码没有错误，则会正常执行，避免异常导致程序中止

##异常的传播  函数中对异常进行处理，则异常不会继续传播
#如果不处理会向函数的调用处传播
# def fn():
#     print("hello fn")
#     print(10/0)
#
# def fn2():
#     fn()
#
# #fn2()
# try:
#     fn()
# except:
#     print("aaa")

#直到传递到全局作用域，如果依然没有处理则停止程序

#当程序出现异常的时候，所有的信息保存在专门的异常对象中，而异常转播时，实际上就是异常对象抛给了调用处

#print(NameError)


print("qqqq")
a = []
try:
    #print(c)
    a[2]
    print(10/0)
except NameError:
    #如果except后不跟任何的内容会捕获所有的异常
    print(" name error")
except ZeroDivisionError:
    print("zero error")
    #r如果except 后面为Exception会捕获所有的异常
except Exception as e:
    print("未知异常",e)
    #无论是否出现异常代码都会执行
finally:
    print("finally")
print("bbb")

class FuException(Exception):
    pass

#抛出异常
def add(a,b):
    if a<0 or b<0:
        #抛异常是为了告诉外部，这里的调用出现问题，希望处理一下
        raise FuException("不能由负数")
    r = a+b
    return r
add(1,-1)