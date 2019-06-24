a =10
b =20

#模块私有的属性_ 使用_模块不能找到
_c = 30



def test():
    print("test123")


class Person:
    def __init__(self):
        self.name ="swk"

#编写测试代码
#test()
if __name__ == '__main__':
    test()