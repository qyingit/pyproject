#函数式编程
#函数在运行的时候创建
#函数作为参数传递
#函数作为返回值返回

#高阶函数
#两个特点：
#接受一个或多个函数作为参数
#将函数作为返回值返回

l = [1,2,3,45,6,7,8,9]

#定义函数,将泪飙中的偶数返回到一个新的列表返回
# def fn(lst):
#     '''
#     fn将指定列表的所有偶数互殴出来，保存到一个新列表中返回
#     定义函数检查是否偶数
#     :param lst:
#     :return:
#     '''
#     new_list =[]
#     for n in lst:
#         if n %2 == 0:
#             new_list.append(n)
#     return new_list



#定义函数,将泪飙中的偶数返回到一个新的列表返回
def fn(lst,fn2):
    '''
    fn将指定列表的所有偶数互殴出来，保存到一个新列表中返回
    定义函数检查是否偶数
    :param lst:
    :return:
    '''
    new_list =[]
    for n in lst:
        if fn2(n):
            new_list.append(n)
    return new_list
def fn2(n):
    if n > 2:
        return True
print(fn(l,fn2))

#filter() 可以从序列中过滤复合条件的元素保存在一个新的列表中
#返回值：
#过滤后的新序列

#fn2作为参数传递进filter函数中
#二fn4实际上只有一个作用，就是作为filter的函数
#filter调用完毕后，fn4就已经没有作用了
#匿名函数lambda函数表达式
#lambda专门创建一些简单的函数，他是函数创建的有一种方式
#语法L: lambda 参数列表： 返回值1

print(list(filter(fn2 , l)))


def fns(a,b):
    return a+b
print((lambda a,b : a+b)(10,20))

#可以见匿名函数赋值给一个变量
fn4= lambda a,b : a+b

print(fn4(10,40))

r = filter(lambda x:x%3==0,l)
print(list(r))

#map函数 可迭代的对象做制定操作
r = map(lambda x:x+1,l)
print(list(r))

#sort方法  对列表中的元素排序
#sort可以接受一个关键字参数，key
#每次都会以列表中的一个元素作为参数来调用，并且使用函数的返回值来比较元素的大小
l = ['bb','aaa','c','dddddd']
l.sort(key=len)

l = [2,3,4,'1','5']
l.sort(key=int)
print(l)

#sorted()函数与sort()函数一致，但sorted可以对任意羞恶进行排序
#使用sorted会返回一个新的对象
print(sorted(l,key=int))


#闭包，将函数作为返回值返回
def fn():
    #函数内部定义函数
    def fn2():
        print("fn2")
    return fn2
r = fn()
#r是一个函数，是调用fn()后返回的函数
#这个函数事在fn()内部定义，并不是全局函数
#所以这个函数总是能狗访问到fn()函数内的变量
#这种高阶函数为闭包
r()

#求多个数的平均值
nums = [20,304,5043,2]
print(sum(nums)/len(nums))



#创建一个函数计算平均值

def make_avg():
    nums = []
    def avg(n):
        nums.append(n)
        return sum(nums)/len(nums)
    return avg
avg = make_avg()
#闭包的作用防止全局变量被局部变量修改
print(avg(10))
print(avg(10))
# 闭包的条件
# 1函数嵌套
#内部函数作为返回值
#内部函数必须要使用外部函数的变量


#装饰器
#创建函数
def add(a,b):
    '''
    和
    :param a:
    :param b:
    :return:
    '''
    return a+b
def mul(a,b):
    print("计算开始")
    r =  a*b
    print("计算结束")
    return r

print(add(10,20))
print(mul(10,20))
#希望函数在计算前打印开始计算，结果计算后打印计算完毕
#即相当于动态代理
#开闭原则:程序的设计，要求对程序的扩展开放，关闭对程序的修改

def fn2(a,b):
    print("kaishi")
    r = add(a,b)
    print("jieshu")
    return r
r = fn2(10,20)


#创建一个函数，自动帮我们生成函数


def fn3(old):
    '''
    用来对其他函数进行扩展,使其它函数执行前开始打印，执行后打印执行结束
    :return:
    '''
    def new_function(*arge,**qqe):
        print("开始执行")
        r = old(*arge,**qqe)
        print("执行结束")
        return r
    return new_function

#像f3的函数称为装饰器,可以不通过修改原来函数的情况进行扩展
@fn3
def sqy():
    print("aaa")

sqy()

f = fn3(add)
r = f(12,32)
print(r)
#可以指定多个装饰器，从内向外的模式进行装饰，就是@最下面的先使用

