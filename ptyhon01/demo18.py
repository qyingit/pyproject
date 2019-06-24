#文件的操作
#i/o操作 input output
#操作文件步骤  1.打开文件  2对文件操作 3关闭文件

#使用open函数打开文件 file 我呢见名字
#同一目录用文件名
# file_name = 'de.txt'
# file_obj = open(file_name)
#
# #读取文件
# con = file_obj.read()
#
# print(con)


#文件的关闭
# file_obj.close()


# con = file_obj.read()
# print(file_obj)


#with 与as的语句
#再with语句中可以直接是u用file——obj读取文件
#一旦with结束文件会自动close
# with open('de.txt') as file_obj:
#     print(file_obj.read())

# try:
#     with open('de.txt') as file_obj:
#         #读文件的内容
#         print(file_obj.read())
#         #
# except FileNotFoundError:
#     print("filename wenjian 不存在")

#open 打开文件由两种形式  1 纯文本文件  2二进制文件
# try:
#     #utf-8编码打开 open默认的编码为None
#     #处理文本文件指定编码 utf-8
#     with open('de2.txt',encoding="utf-8") as file_obj:
#         #读文件的内容
#         print(file_obj.read())
#         #
# except FileNotFoundError:
#     print("filename wenjian 不存在")

#
# try:
#     with open('de2.txt',encoding="utf-8") as file_obj:
#         #将文本文件的全部内容读取，如果读取大文件，一次将大文件加载到内存
#         # ，导致内存泄漏,所以大文件不用调用read()  read(size)
#         #read中可以接受size接受参数  该参数用来指定尧都区的字符的数量
#         #为size指定一个值，每次读取都是从上一次读取的位置读取
#         #如果读取到文件的最后会返回空串
#
#         content = file_obj.read(2)
#         content = file_obj.read(2)
#         print(content)
#         print(len(content))
#         #
# except FileNotFoundError:
#     print("filename wenjian 不存在")


# try:
#     with open('de2.txt',encoding="utf-8") as file_obj:
#         chunk = 1
#         while(True):
#             content = file_obj.read(chunk)
#             print(content,end="")
#             if not content:
#                 break
# except FileNotFoundError:
#     print("filename wenjian 不存在")





# try:
#     with open('de2.txt',encoding="utf-8") as file_obj:
#         #读取一行
#        #print(file_obj.readline())
#         #读取一行内容，会一次性将读取的内容封装到列表中
#         #print(file_obj.readlines())
#         #直接for循环读取
#         for t in file_obj:
#             print(t)
# except FileNotFoundError:
#     print("filename wenjian 不存在")

#文件的写入
# try:
#     #文件的操作 读r 写w 文件存在清空 文件不存在则创建
#     #追加 ，读取文件不能写入 调用str 将数字转为字符串 换行需要用\n
#     #写入完成后write会返回写入字符数的个数
#     #+ 为操作符增加功能 r+ 可读可写  w+可写可读  a+
#x 为新建文件
#     with open('de2.txt',encoding="utf-8",mode="a") as file_obj:
#         r = file_obj.write("\nhello qying!")
#         print(r)
#         #
# except FileNotFoundError:
#     print("filename wenjian 不存在")
# print("ok")


#二进制文件的操作  t文本文件  b二进制文件
# with open("C:/Users/qying/Desktop/那些理财路上踩过的坑(综合版).pptx","rb") as file_obj:
#     #print(file_obj.read(100))
#     new_name = "a.pptx"
#     with open(new_name,"wb") as new_obj:
#         chunk = 1024*100
#         while True:
#             content = file_obj.read(chunk)
#             #内容读取完毕终止循环
#             if not content:
#                 break
#             new_obj.write(content)


#二进制得读取
# with open("de2.txt","rb") as file_obj:
#     print(file_obj.read(100))
#     #获取当前读取得位置
#     print("当前读取",file_obj.tell())
#     #seek修改读取文件得位置
#     #第一个是要切换到得位置
#     #地位个 计算位置方式
#        #可选值 ：
#        #seek(80,0)
#        #0从头计算
#        #1从当前位置计算
#        #2从最后位置开始计算
#
#     print(file_obj.seek(20))
#     print(file_obj.seek(20,0))
#     print(file_obj.seek(20,1))
#     print(file_obj.seek(-20,2))
#     #seek对文本文件得utf-8要注意一个中文是三个字节
#     print("当前读取",file_obj.tell())


#文件得操作
import os
print(os.listdir())

#获取当前目录
#os.getcwd()

#切换目录
#os.chdir("../")

#创建目录
#os.mkdir("aaa")

#删除文件
#os.remove("aaa")

#删除目录
#os.rmdir()

#重命名
#os.rename("","")