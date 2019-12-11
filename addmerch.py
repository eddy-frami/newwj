#encoding=utf-8
import unittest
from upfile01 import upfile0101
from addaccount import addact01
from globle import  globle1
suite = unittest.TestSuite()
g3=globle1()
suite.addTest(globle1('init'))
# gl.__init()
g3.set_value('merchID','S9991007')
g3.set_value('shopRegName','河马付提现07')
g3.set_value('orderCode','110108001445941010')
# g3.set_value('account1','1')
g3.set_value('businessLicense','110108010771594004')
g3.set_value('hmfShopNo','S9991007')
g3.set_value('idNo','257356141')


# globals()['merchID']='S8991674'
# globals()['shopRegName']='河马付一期74'
# globals()['orderCode']='19012309000200000701'
# globals()['businessLicense']='110108016880542'
# globals()['hmfShopNo']='S8991674'
# globals()['idNo']='49236976X'
suite.addTest(upfile0101('upfile01011'))
suite.addTest(addact01('addac0101'))

unittest.TextTestRunner().run(suite)