#序列的方法

ser = [1,321,3,4,12]
# append向列表最后添加元素
ser.append(21)
# insert 向指定位置插入元素
ser.insert(1,90)

#使用新的序列扩展当前队列，类似于extend
ser.extend([0,0])

# clear清空序列，对于可变的元素
#ser.clear()

#pop 删除元素 删除最后的一个元素
dd=ser.pop()
print(dd)


#remove 删除指定的值，根基指定的值删除，只会删除第一个值
ser.remove(90)

#reverse反转
ser.reverse()

#sort对列表种的元素排序 默认升序  reverse=True降序排列
ser.sort(reverse=True)
print(ser)

#遍历列表
# i = 0
# while (i<len(ser)):
#     print(ser[i])
#     i+=1
# else:
#     print("输出完成")

#for循环遍历
#语法  for 变量 in 序列：
#           代码块
#for循环根据序列种的元素去执行，每执行一次会将序列种的元素赋值给元素
for s in ser:
    print(s)