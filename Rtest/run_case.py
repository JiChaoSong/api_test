#conding:utf-8
import unittest
from lie import case

import HTMLTestReportCN


suite = unittest.TestSuite()

suite.addTest(case('test_testfun'))

#unittest.TextTestRunner().run(suite)

st = open('C:/Users/阮家卫/PycharmProjects/untitled/html/case.html','wb')

HTMLTestReportCN.HTMLTestRunner(stream=st,title='学智云接口自动化项目',tester='阮家卫').run(suite)