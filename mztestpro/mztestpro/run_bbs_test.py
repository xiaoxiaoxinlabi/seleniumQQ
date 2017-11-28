from HTMLTestRunner import HTMLTestRunner
import unittest
import time
import os


if __name__ =="__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './bbs/report/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream = fp, title = "QQ登录测试报告", description = "")
    discover = unittest.defaultTestLoader.discover('./bbs/test_case/', pattern = '*_sta.py')
    runner.run(discover)
    fp.close()


