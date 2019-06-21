#流程控制语句
#python从上至下一次执行
#流程控制语句 1 条件判断语句 (if) 2循环语句
# 语法  if 条件表达式 ：语句  if执行时，先对条件表达式进行求职判断
if True : print("aaa")
# 默认情况只管紧随其后的语句
# 为了要执行多条语句，可以使用代码块，为代码分组的机制
#使用缩进作为代码块相当于一段一段的话，代码恢复缩进时缩进级别结束
num = 10
if num > 10 : print("yes")
if False :
    print("wqeq")
    print(1+3)
else:
    print("qying")
# if  10 <15<20 相当于and  缩进四种方式 tab与4个空格


#Input 获取用户的输入
#a = input('--->')
a = "saas"
if a == "admin":
    print("you are admin")
else:
    print("false")

#Input 获取用户的输入年龄
aa = input('年龄:')
aa = int(aa)
if aa > 19:
    print("壮年")
elif aa == 18:
    print("成年")
else:
    print("未成年")