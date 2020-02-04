__author__ = 'hanlingzhi'

'''
create_date: 
    2019.4.3
usage: 
    计数器
'''

class SpiderCounter:

    n = 0

    def __init__(self):
        self.n = 0
        pass

    def create_counter(self):
        self.n += 1
        yield self.n                 # 一定要将生成器转给一个(生成器)对象,才可以完成,笔者第一次做,这里一直出问题,

    def add(self):                   # 再定义一内函数
        return next(self.create_counter())       # 调用生成器的值,每次调用均自增

    def total(self):
        return self.n

