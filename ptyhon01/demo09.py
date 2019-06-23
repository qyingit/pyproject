#help()方法 是pytnon的内置函数
# 通过help()函数可以查询python中的函数用法
# 语法:help(函数对象)

#help(print)


#文档字符串(doc str)
#定义函数时,可以在函数内部编写文档字符串，文档字符串就是函数的说明
#编写文档字符串时,就可以通过help()函数查看函数的说明
#文档字符串非常简单,其实直接在函数的第一行写一个字符串就是文档字符串

#a:int 中的int不是必要的  str也不是必要的
def fun(a:int,b:bool,c:str="hello")->str :
    '''
    文档字符串实列
    :param a:
    :param b:
    :param c:
    :return: 返回值
    '''
    return 10
help(fun)


#函数的作用域与命名空间
#作用域(scope)
#作用域指变量生效的区域

a=20
def fn():
    a =10
    print("函数内部:","a=",a)

fn()
print("函数外部：","a=",a)

#两种作用域：
#1.全局作用与
#  -全局作用域在程序执行的时候创建，在程序执行结束的时候销毁
# - 所有函数以外的区域都是全局作用域
# - 在全局左右域定义的变量就是全局变量，可以在程序的任意位置访问


#函数作用域
# - 函数调用的时候创建，函数调用结束的时候销毁
#每调一次函数就会产生一个新的作用域
#在函数内部调用的变量，都是局部变量，只能在函数的内部访问

def fn2():
    a = 30
    def fn3():
        print("fn3中:",'a=',a)
    fn3()
fn2()

#当使用一个变量时，会优先在当前作用于中寻找该变量，
# 如果有则使用,如果没有则继续去上一级作用于中寻找，如果有则使用，
# 以此内推，如果没有就会报错，抛出异常 nameError : name a is defined

def fn3():
    #a =10
    #在函数中为变量赋值的时候，默认都是为局部变量赋值
    # 如果希望在函数内部修改全局变量,则需要使用global关键字，来声明变量
    global  a
    a =10
    print("a=",a)

fn3()
print(a)



#命名空间namespace 变量存储的位置
#每一个变量都需要储存到指定的命名空间当中
#全局命名空间，用来保存局部变量，函数的命名空间用来保存函数的变量
#命名空间是一个字典，专门用来储存变量
#locals()用来获取当前作用于的命名空间
#如果全局作用于中调用locals()则获取全局命名空间，如果函数作用域中调用locals
#则返回函数的命名空间

locals = locals()
print(locals)
print(a)
print(locals["a"])

#像scope中添加一个key_value，相当于全局中添加
locals["c"] =20
print(c)

def fn4():
    b =10
    #locals = locals()
    #locals["a"]="aaa"
    #获取全局命名空间，globals函数可以用来在任意位置获取全局命名空间
    gbal  = globals()
    print(gbal)

fn4()



#函数的递归

#10的阶乘

def ff(a):
    if a == 1:
        return 1
    else:
        return ff(a-1)*a
aa = ff(10)
#递归将大问题分解为小问题，知道无法分解
#两个条件 1：极限条件  2： 递归条件  将问题继续分解
#递归与循环可以相互代替
print(aa)


#联系
def power(n,i):
    if i == 1:
        return n
    else:
        return n * power(n,i-1)

print(power(10,2))


def hui_wen(s):
    '''检查字符串是不是会问字符串'''
    if len(s)<2:
        return True
    elif s[0] != s[-1]:
        return False
    return hui_wen(s[1:-1])

print(hui_wen("sadfas"))
