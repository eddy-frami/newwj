#encoding=utf-8
import requests
import json
import unittest
class globle1(unittest.TestCase):
    # 在类里面，方法外面，先声明一个字典。如果在某方法里面赋值，那么这个字典只能在方法里面用
    merchIDlist = {}
    def init(self):
        global merchIDlist


    #     设置set函数给字典的字段赋值
    def set_value(self,merchID,value):
        self.merchIDlist[merchID]=value

    #     设置get函数，取出来字典里某字段的值
    def get_value(self,merchID):
        return self.merchIDlist[merchID]
