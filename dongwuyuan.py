# -*- coding: cp936 -*-
#by liuxianwei qq����:514694967@qq.com
#https://github.com/ericliuxw/python/blob/master/dongwuyuan.py
z=6
z=3#�������������ݣ�����˼�壬�仯�����������ڲ�ͬ�ĵط�������ȡ��ͬ��ֵ
def test(hi):#������������Ϊ;hi�ǲ�����ʹ��ʱ���������벻ͬ������
    ''
    ""
    print('hello world',hi)
class laohu1(object):#��ɫ����ɫ��ۺ죩����python�ؼ��֣���python�����ĵ��ʣ�����ֻ���ڹ涨�Ĺ̶��ط�ʹ�á�
    '''����һֻ�ϻ�'''
    def test(self,hi):#class ��������һ��������࣬def ��������һ���������Ϊ  
        print('hello world',hi)
    def __init__(self,mingzi,zhuazi,yanjing):#�����»��߿�ͷ�ͽ�β��Ҳ��python�Ĺؼ��֣�������д��Ӳ���
        '''��ʼ�������������ʱ�������ֵ�'''
        self.__mingzi=mingzi
        self.__zhuazi=zhuazi
        self.__yanjing=yanjing
        self.yanse='hong'#����,������������,���ݸ���Ĳ�ͬ,ȡ��ͬ��ֵ,���Ǻ�ɫ='hong',С���ǻ�ɫ='huang'
    def run(self):#self�����ǵ���������������
        '''��Ϊ���ܶ�'''
        print('pao')
        return 0
    def eat(self):
        '''��Ϊ���Զ���'''
        print('chi')
        return 0
    def getMingzi(self):
        '''��Ϊ���鿴���������'''
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
    
##########################      ��������ʽ�Ĵ���          ##############################
    
class dongwu(object):
    '''����һ�ද��'''
    __count=0#�������
    count=0
    def __init__(self,mingzi,zhuazi,yanjing):
        '''��ʼ�������������ʱ�������ֵ�'''
        self.__mingzi=mingzi
        self.__zhuazi=zhuazi
        self.__yanjing=yanjing
        self.yanse='heise'
        dongwu.__count=dongwu.__count+1#���������
    def run(self):
        '''�ܶ�'''
        print('pao')
        return 0
    def eat(self):
        '''�Զ���'''
        print('chi')
        return 0
    def getMingzi(self):
        '''�鿴���������'''
        return self.__mingzi
    def __test(self):
        '''����˽�з���'''
        print('testaaa')
    
    
    @staticmethod
    def getcnt():
        '''��̬��������ȡ���ж���ĸ���'''
        return dongwu.__count
    @staticmethod
    def plus():
        '''��̬������������������˹����һ��'''
        dongwu.__count=dongwu.__count+1#���������
class laohu6(dongwu):
    pass
class laohu(dongwu):
    '''����һ���ϻ�'''
    def run(self):
        '''�ܶ���ʵ��������5��'''
        print('pa 5 bu')
        return 0
    
class laoying(dongwu):
    '''����һ����ӥ'''
    def __init__(self,mingzi,zhuazi,yanjing,chibang):
        super(laoying,self).__init__(mingzi,zhuazi,yanjing)
        self.__chibang = chibang
    def run(self):
        '''�ܶ���ʵ�����Ƿ�5��'''
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

#��Ԫ����
if __name__ == '__main__':
    x=laohu('hu1',4,2)
    y=laoying('ying6',2,2,2)
    print(y.count,y.getcnt())
    #print(y.__count)
    
##    print(dir(object),'---$$$----')
    #print(help(object),'---$$$----')
    print(help(laohu),'----$$$---')   

    #��̬
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
##    #print(z.__mingzi)#˽�б���
##    #print(z.__test())#˽�к�������
