# -*- coding: cp936 -*-
class laohu6(object):
    def __init__(self,mingzi,zhuazi,yanjing,weiba):
        self.__mingzi=mingzi
        self.zhuazi=zhuazi
        self.yanjing=yanjing
        self.weiba=weiba
    def run(self):
         print('pao')
         return 0
    def eat(self):
        print('chi')
        return 0
    def getMingzi(self):
        return self.__mingzi

class dongwu(object):
    '''����һ�ද��'''
    count=0#�������
    def __init__(self,mingzi,zhuazi,yanjing):
        self.__mingzi=mingzi
        self.zhuazi=zhuazi
        self.yanjing=yanjing
        dongwu.count=dongwu.count+1#���������
    def run(self):
         print('pao')
         return 0
    def eat(self):
        print('chi')
        return 0
    def getMingzi(self):
        return self.__mingzi
    def __test(self):
        print('testaaa')
    
    
    @staticmethod
    def getcnt():
        return dongwu.count
    @staticmethod
    def plus():
        dongwu.count=dongwu.count+1#���������
class laohu6(dongwu):
    pass        
class laoying(dongwu):
    '''����һ����ӥ'''
    def __init__(self,mingzi,zhuazi,yanjing,chibang):
        super(laoying,self).__init__(mingzi,zhuazi,yanjing)
        self.chibang = chibang
        laoying.count=laoying.count+1
    def run(self):
         print('fly 5 xia')
         return 0
    def eat(self):
        print('tu zi')
        return 0
    
class laohu(dongwu):
    '''����һ���ϻ�'''
    def __init__(self,mingzi,zhuazi,yanjing,weiba):
        '''��ʼ��'''
        super(laohu,self).__init__(mingzi,zhuazi,yanjing)
        self.weiba= weiba
        laohu.count=laohu.count+1
    def run(self):
        print('pa 5 bu')
        return 0
##    def eat(self):
##        print('zhu rou')
##        return 0
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
    x=laohu('hu',4,2,1)
    print(x.run())
    print(x.__dict__)
    y=laoying('ying',2,2,1)
    print y.getcnt()
    x.plus()
    print y.getcnt()
    
    z=laohu6('hu6',4,2)
    print(z.run(),',hu6')

    
    print(dir(laohu))
    print(help(laohu))
    print(laohu.__doc__)
    print(z.getMingzi())
    #print(z.__mingzi)#˽�б���
    #print(z.__test())#˽�к�������

    #��̬
    zx=zoo()
    zx.add(x)
    zx.add(y)
    zx.run()
    #print(laohu.__dict__)
