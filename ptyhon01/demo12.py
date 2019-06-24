#python的类

class Person:
    def say(self):
        print("你好 ",self.name)


#类的属性一般不需要共享的
p1 = Person()
p1.name = "qying"
p2 = Person()
p2.name = "zbj"
p1.say()
p2.say()
#对于person来说每个对象的name属性基本上是不同的
#现在是手动将属性添加到对象中,这种忘记添加属性的时候就会报错
#希望在创建对象的时候必须设置name属性，如果不设置就不会创建，
#不是创建对象后手动完成的


class Person:
    print("person")
    def say(self):
        print("你好 ",self.name)
    #类中定义特殊方法以_开头 _结尾为魔术方法
    #init方法不需要调用类似于构造器
    #特殊的方法在特殊的时刻自己调用
    #特殊方法什么时候调用
    #特殊方法的作用
    def __init__(self):
        print("init")

p1 =Person()

#创建对象流程  1 创建Person 2 内存中新创建一个对象
# 3执行类代码块种的方法 4 init方法执行  4将对象的id赋值给变量

#init 会在对象创建后执行  初始化
#可以向新创建的对象种初始化属性

class Person:
    #在类对象中
    name ="qying"
    def __init__(self,name):
        #在实例对象中
        self.name = name
    def say(self):
        print("你好 ",self.name)

p1 = Person("qying111")
p1.say()
#类的基本结构
 #Class  类名[父类]:
 # 公共属性。。。。
 #对象的初始化方法
 # def _init_(self,name)
 # 其它方法
 # def fun()

class Dog():
    def __init__(self,name,age,gender,height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
    def jiao(self):
        print("wangwang")
    def yao(self):
        print("yaoyaoyao")
    def run(self):
        print("runrunrun")

dog =Dog("wc",18,"nan",1.78)
# 目前可以直接通过对象.属性修改值 涉及私有问题，这种方式导致对象的属性可以随意修改
print(dog)
dog.jiao()

#属性不饿能随意修改
#属性不能改为任意的值,必须是有效的值 如:不能为负数


#对象的封装
#封装指隐藏对象中不希望外部访问的属性或方法
class Dog():
    def __init__(self,name):
        self.hidden_name = name

    def jiao(self):
        print("wangwang")
    def yao(self):
        print("yaoyaoyao")
    def run(self):
        print("runrunrun")
d = Dog("qying1")
d.name = "qying2"
print(d.hidden_name)

#如何隐藏对象的属性  没有绝对安全的隐藏
#改属性名去隐藏对象
#如何获取对象种的属性
# 需要提供一个getter于setter方法
#getter获取指定属性(get_属性名)
class Dog:
    def __init__(self,name):
        self.hidden_name = name
    def say_hello(self):
        print("i am ",self.hidden_name)
    def get_name(self):
        return self.hidden_name
    def set_name(self,name):
        if(len(name)>9):
            self.hidden_name = name

d = Dog("旺财 ")
print(d.get_name())
#使用封装增加类的复杂度，但是确保了数据的安全性，使调用者无法随意修改对象的属性
#可以根据情况使用get于set方法
#使用set与get可以对数据进行校验
d.say_hello()
d.set_name("qying")
d.say_hello()

#封装的优点
class Rectangle:
    def __init__(self,width,hight):
        self.hidden_width =width
        self.hidden_hight = hight
    def get_width(self):
        return self.hidden_width
    def set_width(self,width):
        self.hidden_width = width
    def get_highth(self):
        return self.hidden_hight
    def set_hight(self,hight):
        self.hidden_hight = hight
    def get_areas(self):
        return self.hidden_width*self.hidden_hight
r = Rectangle(2,3)
print(r.get_areas())
#使用get可以获取一些计算的属性


#__可以为对象的属性使用__
#这种只能通过内部访问


class Dog:

    def __init__(self,name):
        self.__hidden_name = name
    def say_hello(self):
        print("i am ",self.__hidden_name)
    def get_name(self):
        return self.__hidden_name
    def set_name(self,name):
        if(len(name)>9):
            self.__hidden_name = name

dog = Dog("qying")
#双下划线是py自动为属性改了一个名字。实际上将名字改为了,_类名_属性名  比如__name->_Dog_name
#一般不采用__ 就用一个下划线就可以了 _  约定下划线开头为私有属性
#没有特殊需求不要改私有属性

#property装饰器

class Dog:

    def __init__(self,name):
        self._hidden_name = name
    def say_hello(self):
        print("i am ",self._hidden_name)
    @property
    def name(self):
        print("111")
        return self._hidden_name
    @name.setter
    def name(self,name):
        self._hidden_name = name

dog = Dog("qying")

print(dog.name)
#setter方法的装饰器 可以通过属性的方式修改值
#@属性名.setter
dog.name="qying111"
#有setter则必须要有getter
print(dog.name)



#对象的继承
class Animal:
    def run(self):
        print("run")
    def sleep(self):
        print("sleep")

#继承 ： 一个类从其它类获取属性与方法
#语法: class A(父类);
#子类有父类的所有属性与方法
class Dog(Animal):
    def bark(self):
        print("汪汪")


dog  = Dog()
dog.run()
class Ha(Dog):
    pass
ha = Ha()
print(isinstance(dog,Animal))
print(isinstance(ha,Animal))
#object 是所有类的父类
print(issubclass(Dog,Animal))

#方法的重写，如果本类没有方法回一次查找，知道找到可用的方法s
class Dog(Animal):
    def bark(self):
        print("汪汪")
    #子类覆盖父类的方法
    def run(self):
        print("狗 run")

dog = Dog()
dog.run()



#对象的继承
class Animal:
    def __init__(self,name):
        self._name = name
    def run(self):
        print("run")
    def sleep(self):
        print("sleep")
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name= name

class Dog(Animal):

    def __init__(self,name,age):
        #调用父类的init进行初始化
        #super获取当前的父类,不用传self
        super().__init__(name)
        self.age = age

    def bark(self):
        print("汪汪")
    #子类覆盖父类的方法
    def run(self):
        print("狗 run")

#父类的所有方法都会被子类继承 ，包括特殊方法
d= Dog("qying111 ",18)
print(d.name)


#多重继承
class A(object):
    def test(self):
        print("aaa")
class B(object):
    def test2(self):
        print("bbb")
    def test(self):
        print("bbb1")
class C(A,B):
    pass

#__bases__获取当前类的所有父类
print(C.__bases__)#(<class '__main__.B'>,)
print(B.__bases__)

#在python可以为一个类指定多个父类
#多重继承会使子类有多个父类，并且会获取所有父类中的方法

print(C.__bases__)

#在开发中应该精良避免多重继承，多重继承会使代码过于复杂
c = C()
c.test()
#如果两个父类有相同的方法会根据顺序查找类及父类种是否有方法去查找方法
c.test2()


#多态是面向对象的三大特征
#多态即有多种形态
class A:
    def __init__(self,name):
        self._name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name

class B:
    def __init__(self,name):
        self._name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name
    def __len__(self):
        return 10

a = A("swk")
b = B("zbj")

#对于sayhello只要对象中含有name水星，就可以作为参数传递
#这个不考虑对象类型，只要有name属性
def say_hello(obj):
    print("你好",obj.name)
say_hello(a)
say_hello(b)


def say_hello2(obj):
    #可以增加类型检查，导致函数只适应一类的对象，无法处理其他类型的对象，这样导致函数适应性差
    if isinstance(obj,A):
        print("你好",obj.name)
say_hello2(b)

#鸭子类型  多态
#如果一个人走路像鸭子，叫声像鸭子，那就是鸭子
#isinstance（）一般是不会使用的
print(len(b))

#封装保证数据的安全性
#继承保证对象的可扩展性
#多态保证程序的灵活性