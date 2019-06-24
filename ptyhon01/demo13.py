#类方法 @classmethod  cls就是类对象
class A:
    @classmethod
    def say(cls):
        print("sadaf")
    #静态方法 不需要指定默认参数，可以通过类与实例去调用
    @staticmethod
    def test1():
        print("static")
A.say()
A.test1()
#静态方法只是保存到当前类的函数,相当于一个普通的函数
#静态方法一般只是一些工具方法，和当前类无关


#py的垃圾回收
#程序的垃圾影响程序的性能，所以垃圾需要及时清理
# 没有用的东西就是垃圾

class A:
    def __init__(self):
        self.name = "A类"

    #__del__在垃圾回收的时候调用
    def __del__(self):
        print("回收",self)
a = A()
# b = a
print(a.name)
a = None #将a设置为None,没有任何的变量对A()进行引用，着就会变为垃圾

#垃圾对象占用内存过多，需要及时删除
#py有自动垃圾回收机制，会自动将没有引用的对象删除

# 判断对象是不是垃圾，对象是否有被变量引用
#input("shuru :")

#特殊方法  魔术方法 使用__开头和结尾的方法
#特殊方法不选哟手动调用，需要在特殊的情况下执行

#__new__ 对象创建的时候调用

#
class Person:
    def __init__(self,name,age):
        self.name =name
        self.age = age
    #这个特殊方法尝试将对象转为字符串的时候调用
    def __str__(self):
        #return self.name+":"+str(self.age)
        return "Person[name=%s,age=%d]"%(self.name,self.age)
    #对对象使用__repr__函数调用，指定对象在交互模式中输出的对象 如果写a直接输出
    def __repr__(self):
        return "hello"

    #比较大于小于，在对象比较大于的时候调用
    #lt le eq ne gt ge
    def __gt__(self, other):
        return self.age > other.age
    ##len 获取对象长度
    #__bool__转为bool值
    def __bool__(self):
        return self.age>16
    ##__add__ 对对象做加法减法一系列算术方法


p1 = Person("swk",18)
p2 = Person("zbj",18)

#打印对象那个的时候，实际上是调用__str__()的返回值
print(repr(p1))
print(p1 > p2)
print(p1)
if p1:
    print("成年")