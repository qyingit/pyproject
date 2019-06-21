#序列

## 列表(list)，python中的一个对象
# 对象就是内存中专门存储数据的区域
# 之前的对象，像数值，只能保存一个单一的对象
# 而列表可以保存多个有序的数据


# 列表的创建，通过 [] 进行创建
my_list = []
print(type(my_list))

#列表储存的数据为元素，一个列表可以储存多个元素
list1 = [10,20]
print(list1,type(list1))
# 列表可以保存任意的对象
list2 = ["eqw",12,32]

# 列表按插入的顺序储存
print(list2)

#获取列表的数据，通过索引获取列表中的元素,索引从0开始，使用[]获取
print(list2[1])
#print(list2[7])# IndexError: list index out of range 索引超出范围

#获取列表长度  len()
print(len(list2))

#列表切片  从现有列表获取一个子列表
# 如果索引是负数，则从后向前获去元素
#语法: 列表[起始:结束],包含起始位置不包含结束位置
#切片不影响原来的元素
#如果省略开始位置，则一直截取到最后,若都省略，相当于创建了一个副本
print(list2[1:4])


# 语法  列表【起始:结束:步长】 步长表示每次获取元素的间隔
#步长不能为0，可以是负数，列表倒转从后往前取数据
print(list2[::2])




# 数据的通用操作
# + 和 * 号的操作 字符串相加
my_list = list2 +list1
print(my_list)
print(my_list * 2)
#in与not_in 检查列表函数是否存在于列表中
print(12 in my_list)
print(13 not in my_list)

#len() 获取长度的个数

#min() max() 获取元素的最大最小值
my_list = [12,23,435,565,12,74]
print(min(my_list))

#两个方法  index() count() 必须通过对象.方法调用
# index(a,x,y)第二与第三个元素标志范围
print(my_list.index(12,2))#ValueError: 24 is not in list
print(my_list.count(23))

#数据结构是计算机中数据储存的方式
# 序列用于保存一组有序的数据，所有的数据在序列中各有一个唯一的位置,序列会按照添加的顺序分配索引
# 可变序列（序列中的元素可以改变）
    #列表(list)
# 不可变序列:
   #字符串
   #元组(tuple)

# 创建列表
stus = [1,2,3,4,45,6,]
#修改元素
stus[0] = 3
#删除元素
del stus[0]
print(stus)
#通过切片修改列表 切片赋值只能使用序列
stus[1:2]=[123,21]
#替换元素
stus[1:1]=[123,21]
#当设置步长时切片的元素需要等于序列的原属
print(stus)
stus[::2]=[222,222,111,111]
print(stus)
del stus[0:3:2]
print(stus)

