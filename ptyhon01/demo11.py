# 对象

#s什么是对象是，是内存中存储数据的区域
#对象可以村方各种数据
#对象由标识 id 类型type 值value
#python中所有的操作都是通过对象来进行的
#面像过程的编程语言，指将程序的逻辑分解为一个一个的步骤，通过步骤来完成程序
#面向过成只适用于功能，们可复用性低


#类的对象class  python的内置对象 内置对象不够，需要自定义一些对象
# 创建对象  a = int(10) 不用a= 10
#大驼峰法命名类
#类的语法
# class 类名([父类]):
class MyClass:
    pass

#print(MyClass)
#使用MyClass创建一个对象，就像调用一个函数
mc = MyClass() #mc就是Myclass创建的对象，就是一个实例
mc1 = MyClass()

print(mc,type(mc))
print(mc1,type(mc))

result = isinstance(mc,MyClass)
print(result)

#类也是一个对象
#类就是一个用来创建对象 类是一个type类型的对象

#对象的创建流程
#创建一个变量mc
#在内存中创建一个新对象
# id 系统分配  type 指定哪个class  将对象的id赋值给变量
#通过Myclass创建对象是一个空盒子
#可以像对象中添加变量，对象的变量为属性
mc.name = 'swk'

print(mc.name)

#类的定义
#类由属性跟函数构成

class Person:
    #在代码块中可以定义变量跟函数
    a=10
    b=20
    #类中i当以的函数为方法
    def say_hello(self):
        print("hello"+self.name)
p1 = Person()
print(p1.a)
#调用方法
#p1.say_hello()
#方法调用和函数调用的区别如果使函数调用，传几个参数，就会有几个实参
#但是方法中，默认传递一个函数，所以方法中至少有一个形参

#变量会成为该类实例的公共属性，所有该类实例都可以通过对象名，属性名的形式访问
#函数会成为该类实例的而公共方法,所有该类实例都可以通过对象，方法名()的方法调用


#实例如何访问类中的属性与方法
#类中定义的属性与方法都是公共的，任何该类实例都可以访问
#属性和方法查找的流程
#当调用对象的属性使，解析器会现在当前对象中寻找是否包含该属性
#如果有，则直接返回当前对象的属性指
#如果没有，则去当前对象中寻找，如果由则但会对象的属性值
#如果没有会报错
p2 = Person()
p1.b = 40
print(p2.b)

#如果所有的属性使共享的，则应该存储到类中，如果使独有的则保存到实例对象中

#在方法中不能直接访问类中的属性
#方法每次调用会自动传递一个对象,就是该调用对象本身，一般该方法叫self

p1.name = "qying"
p1.say_hello()