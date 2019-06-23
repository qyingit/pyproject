# range 是一个函数  可以用来生成一个自然数羞恶
r = range(5)#[0, 1, 2, 3, 4]
print(r)
print(list(r))

#该函数需要三个函数
#1.起始位置
#2.结束位置 3
# .步长
r = range(10,0,-1)
print(list(r))

#通过range可以创建一个执行制定次数的for循环
#for 除了创建方式，其余都跟while一样，并且for循环使用比较简单
for i in range(10):
    print(i)

for s in "hello":
    print(s)
# 元祖 不可变的序列，操作方式等同于列表
# 一般希望数据不可变时使用列表
#创建元祖

#使用()
my_tuple = (1,2,1,2,2)
print(my_tuple[3])
#不能尝试对元祖中的元素赋值
#当元祖不是空元组时，括号可以省略
my_tuple =1,2,3,4,5
# 元祖不是空元祖，他里边至少有一个,
print(my_tuple)
#特殊用法
my_tuple = 10,20,304
a,b,c = my_tuple
print(a)
#元祖的解包,值得就是将元组中的每一个元素都赋值给一个变量
a=100
b=80
a,b=b,a
print(a,b)

# 在对元祖解包时，其原属个数必须相等,如果不足的可以用*，这样变量会互殴去元祖中所有的值
a,*b = my_tuple
*a,b =my_tuple
print(b)


##可变对象
#对象的值可以改变

# == 与is 的区别
# == 与！= 比较的时对象的值
#is is not 比较对象的值是不是同一个对象
a = [1,2,3]
b = [1,2,3]
print(a==b)
print(a is b)

##字典的操作  字典属于新的数据结构mapping 作用跟列表差不多
# 列表存储数据的性能很好，但查询的性能很差
# 在字典中每一个元素都有一个唯一的名字，通过唯一的元素可以找到某个字，查询元素效率比较快雷士与map
#字典唯一的名字较key，对象为value，键值对的结构
# 通过key可以快速的查询value 每一个键值对为item


#字典的创建 {}
d = {}

#字典的key是不可变对象
#字典的值可以是任意对象
#字典的额键是不能狗重复的，后面的建会替换前面的键
d = {'name':'qying','age':12,'gender':'男'}
print(d)
#一般字典的键为字符串 ,通过名字可以获取字典的值
print(d['name'])
#如果使用字典不存在的键会报错
# print（d["hello]）

#字典的使用

#创建方式
# 1 {k1:v1,k2:v2}
#2 使用dict(name="dfs")函数，字典创建的key为字符串
d = dict(name="qying",age="18")
print(d)
#3传一个序列作为参数,将双值地序列转为字典
a = [("name","qying111"),("age",18)]
d = dict(a)
print(d)

# len可以获取键值对的个数
print(len(d))

#in 检查字典中是否包含指定的键,not in 检查字典中是否不包含指定的键
print('hello' in d)

# 获取字典中的值，根据键来获取值
print(d['age'])

n = "name"
print(d[n])

# 通过[]来获取值，如果键不存在，会抛出异常keyError
# get(key[,default])该方法用来根据键来获取字典中的值
print(d.get("name"))
print(d.get("sss"),"sss")
print(d.get("sss","sss"))
#修改字典，如果key存在则覆盖，不存在则添加
d['address']='两路口'
print(d)

#setdefault 像字典中添加key value
d.setdefault("name","猪八戒")
#如果key 已经存在，则返回key值，如果不存在，会设置值
print(d)

#update将其他字典中的keyvalue添加到当前字典中
d1 = {"a":"1","b":2}
d2 = {"b":"3","c":"4"}
d1.update(d2)
print(d1)

#删除字典里面的键值对
del d1['a']
print(d1)
#popitem（）随机删除字典中的一个键值对,一般都会删除最后一个键值对，会返回一个元祖,
a = d2.popitem()
print(d2,a)

#pop根据key删除字典中的item
b=d1.pop("b")
print(d1,b)
#可以传一个默认值进去,如果删不掉会显示默认值
b=d1.pop("b","默认值")
print(d1,b)

#使用popitem删除一个空字典会保报错,del删除不存在会报错

#使用copy，对字典进行浅复制
#赋值以后的对象，与赋值以前的对象是相互独立的，修改一个不会影响另外一个
#注意对象的值，内部有可变对象，这个可变对象内部的值不会被赋值
dd = d.copy()
print(d is dd)

#便利字典 keys() values() items()s
print(d.keys())

for i in d.keys():
    print(i)
print(d.values())
print(d.items())

for k,v in d.items():
    print(k,v)

#集合 set
#集合与列表相似
#不同点  1几何中 之存储不可变对象 ，几何中的对象是无序的  集合中不能出现重复元素

#集合的创建
s = {1,2,3,45,}
#集合中不能放列表 因为列表是不可变的对象
print(s)
s = set()
# 可以通过set将序列与字典转为集合
s = set([1,2,3,4,22,3,3])
s =set((1,2,3,3,2))
s = set("helo")
#使用set将字典转为集合时跟之无关
print(s)

#集合不能通过索引去访问

# in判断集合是不是在几何中

# 使用len获取集合的长度

#s使用add在集合中添加元素
s.add(100)

print(s)

#update将其它集合更新到该个集合中
#update使用传递羞恶或字典作为参数时，字典指挥使用该个键


s.pop()
#删除元素 会返回元素的值
#remove() 删除指定值

print(s)
s.remove("h")
print(s)

#clear 清空集合
#s.clear()
#s.copy()浅复制

# 创建两个集合
#求交集
s= {1,2,3,4,5}
s1 = {3,4,5,6,7}
s2 = s & s1
print(s2)
#并集运算
s2 = s | s1
print(s2)

#差集
s2 = s - s1
print(s2)

#异或集 只在一个几何中出现的元素
s2 = s ^ s1
print(s2)

# 《= 检查一个集合是不是另一个集合的子集

s2 = s <= s1
print(s2)

#<检查一个集合是不是另一个集合的超子集
  
