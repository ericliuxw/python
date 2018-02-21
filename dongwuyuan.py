# -*- coding: cp936 -*-
#by liuxianwei qq邮箱:514694967@qq.com
#https://github.com/ericliuxw/python/blob/master/dongwuyuan.py
z=6
z=3#变量，代表数据，顾名思义，变化的数量，他在不同的地方，可以取不同的值
def test(hi):#函数，代表行为;hi是参数，使用时，可以填入不同的内容
    ''
    ""
    print('hello world',hi)
class laohu1(object):#红色（红色或粉红）代表python关键字，即python保留的单词，我们只能在规定的固定地方使用。
    '''这是一只老虎'''
    def test(self,hi):#class 代表定义了一个对象的类，def 代表定义了一个对象的行为  
        print('hello world',hi)
    def __init__(self,mingzi,zhuazi,yanjing):#两个下划线开头和结尾的也是python的关键字，可以重写添加参数
        '''初始化，即对象出生时的起名字等'''
        self.__mingzi=mingzi
        self.__zhuazi=zhuazi
        self.__yanjing=yanjing
        self.yanse='hong'#变量,代表属性数据,根据个体的不同,取不同的值,大虎是红色='hong',小虎是黄色='huang'
    def run(self):#self代表是单个对象个体的数据
        '''行为：跑动'''
        print('pao')
        return 0
    def eat(self):
        '''行为：吃东西'''
        print('chi')
        return 0
    def getMingzi(self):
        '''行为：查看动物的名字'''
        return self.__mingzi
z=int(3)
z=3
x6=laohu1('hu6',4,2)
x5=laohu1('hu5',4,2)
#x6.__mingzi#(error)
x6.getMingzi()
x6.yanse
class laoying1(object):
    def __init__(self,mingzi,zhuazi,yanjing,chibang):
        self.__mingzi=mingzi
        self.__zhuazi=zhuazi
        self.__yanjing=yanjing
        self.__chibang=chibang
    def run(self):
         print('fei')
         return 0
    def eat(self):
        print('chi')
        return 0
    def getMingzi(self):
        return self.__mingzi
    
##########################      下面是正式的代码          ##############################
    
class dongwu(object):
    '''这是一类动物'''
    __count=0#动物个数
    count=0
    def __init__(self,mingzi,zhuazi,yanjing):
        '''初始化，即对象出生时的起名字等'''
        self.__mingzi=mingzi
        self.__zhuazi=zhuazi
        self.__yanjing=yanjing
        self.yanse='heise'
        dongwu.__count=dongwu.__count+1#动物计数器
    def run(self):
        '''跑动'''
        print('pao')
        return 0
    def eat(self):
        '''吃东西'''
        print('chi')
        return 0
    def getMingzi(self):
        '''查看动物的名字'''
        return self.__mingzi
    def __test(self):
        '''测试私有方法'''
        print('testaaa')
    
    
    @staticmethod
    def getcnt():
        '''静态方法，获取所有动物的个数'''
        return dongwu.__count
    @staticmethod
    def plus():
        '''静态方法，动物计数器，人工添加一个'''
        dongwu.__count=dongwu.__count+1#动物计数器
class laohu6(dongwu):
    pass
class laohu(dongwu):
    '''这是一类老虎'''
    def run(self):
        '''跑动，实际上是爬5步'''
        print('pa 5 bu')
        return 0
    
class laoying(dongwu):
    '''这是一类老鹰'''
    def __init__(self,mingzi,zhuazi,yanjing,chibang):
        super(laoying,self).__init__(mingzi,zhuazi,yanjing)
        self.__chibang = chibang
    def run(self):
        '''跑动，实际上是飞5下'''
        print('fei 5 xia')
        return 0

class zoo(object):
    def __init__(self):
        self.deq=[]
    def add(self,dongwu):
        self.deq.append(dongwu)
    def run(self):
        print('kaishi.....pao.....')
        for i in self.deq:
            i.run()

#单元测试
if __name__ == '__main__':
    x=laohu('hu1',4,2)
    y=laoying('ying6',2,2,2)
    print(y.count,y.getcnt())
    #print(y.__count)
    
##    print(dir(object),'---$$$----')
    #print(help(object),'---$$$----')
    print(help(laohu),'----$$$---')   

    #多态
    zx=zoo()
    zx.add(x)
    zx.add(y)
    zx.run()
    #print(laohu.__dict__)
    
##    z=laohu6('hu6',4,2)
##    print(z.run(),',hu6')
##    
##    print(x.run())
##    print(x.__dict__)
##    print(y.getcnt())
##    x.plus()
##    print(y.getcnt())
##    print(dir(laohu))
##    print(help(laohu))
##    print(laohu.__doc__)
##    print(z.getMingzi())
##    #print(z.__mingzi)#私有变量
##    #print(z.__test())#私有函数方法
