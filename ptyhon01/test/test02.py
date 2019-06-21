a = 7
sum =0
# while a<100:
#     a+=1;
#     if a%2 ==1:
#         sum+=a
# print(sum)

# count =0
# while a<100:
#     a+=1
#     if a%7 == 0:
#         sum += a
#         count+=1
# else:
#     print("sum=",sum,"count=",count)

# break 用来立即退出循环 ，
# continue跳出本次循环
# break与continue只对最近的循环起作用

# pass在判断与循环语句中进行占位
# if a<5:
#     pass


# 引入time模块，统计程序执行的时间
# from 从哪个模块导入
from time import *
# time() 获取当前时间，返回的单位时秒
begin = time()
count =0
while a<10000000:
    a+=1
    if a%7 == 0:
        sum += a
        count+=1
else:
    print("sum=",sum,"count=",count)
# while a<10000000:
#     a+=7
#     sum += a
#     count+=1
# else:
#     print("sum=",a,"count=",count)
end = time()
print(end-begin)
#4.575028896331787  0.8832080364227295