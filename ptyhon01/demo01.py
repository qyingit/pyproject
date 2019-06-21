# 数据类型
# 数值:整数(int 无限大),浮点数(小数)，复数
a = 10
b = 20
c = 43122222222222222222222222222222222
print(c)
# 如果数字长度过大，可以使用下划线
c = 1_2_32
print(c)
# 10进制不能以0开头 二进制0b 八进制 0o  十六禁止0x

# 浮点数进行运算时,可能会有一个不精确的结果


b = 0.1
c = 0.2
print(b+c)

# 字符串:标识一段文本信息，在python中需要使用引号弄起来，可以单引号，可以双引号，不能混合使用，相同的引号不能够嵌套

c= 'as"dsad"das'
print(c)
# 单引号跟双引号不能够跨行使用 使用3重引号标识长字符串,会换行并保留字符的格式

str = """asdafa
fsafsad
123"""
print(str)

#转义字符 \ 作为转义字符
# \uxxxx  标识unicode编码
str = 'das\"daa'
str = 'das\\"daa'
print(str)
# 格式化字符串 ，字符串之间加法运算
a = "213"+"321"
print(a,21213)

#在字符串中可以在字符串中自定占位符
b = 'dasdas %s '%' qying'
b = 'q %s %s' % ("www",'sss')

#最小4个字符，多的用空格补位
b = 'q %4s' % ("www")

#保存一位小数
b = 'q %.1s'% 321432.322
print(b)
# %s 标识任意字符  %f  浮点数占位符  %d 整数占位符
print("a=%s"%b)
# 格式化字符串用f去创建
# 格式化字符串可以直接嵌入变量

str = f"hello {a} {b}"
print(str)
print(f"a={a}")

name = "1ying"
print("欢迎"+name+"光临")
print("欢迎",name,"光临")
print("欢迎%s光临"%name)
print(f"欢迎{name}光临")

#字符串的复制  用乘法会重复到指定的次数后停止
a ='ada'
print(a*20)

