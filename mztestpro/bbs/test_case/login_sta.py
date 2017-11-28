#coding:utf-8

from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit
from models import function
from page_obj.loginPage import Login


class LoginTest(myunit.MyTest):
    '''qq邮箱登录测试'''
  
    def user_login_verify(self, username = "", password = ""):
        Login(self.driver).user_login(username, password)

    def test_login1(self):

        self.user_login_verify()
        po = Login(self.driver)
        self.assertEqual(po.user_error_hint(), "您还没有输入帐号！")

        function.insert_img(self.driver, "user_pawd_empty.jpg")


    def test_login2(self):

        self.user_login_verify(username = "account_name")
        po = Login(self.driver)
        self.assertEqual(po.password_error_hint(), "您还没有输入密码！")
        function.insert_img(self.driver, "pawd_empt.jpg")

    def test_login3(self):
        self.user_login_verify(password = "account_password")
        po = Login(self.driver)
        self.assertEqual(po.user_error_hint(), "您还没有输入帐号！")
        function.insert_img(self.driver, "user_empty.jpg")

    def test_login4(self):
        '''您还没有输入验证码！'''
        character = random.choice('zsdffd')
        username = "zhangsan" + character
        self.user_login_verify(username = username, password = "account_password")
        po = Login(self.driver)
        self.assertEqual(po.password_error_hint(), "您输入的帐号或密码不正确，请重新输入。")

        function.insert_img(self.driver, "user_password_error.jpg")

    def test_login5(self):
        '''用户名，密码正确'''
        self.user_login_verify(username = "account_name", password = "account_password")
        sleep(2)
        po = Login(self.driver)
        self.assertEqual(po.user_login_success(), "One piece")

        function.insert_img(self.driver, "user_password_true.jpg")

if __name__ == "__main__":
    unittest.main()
    #testunit = unittest.TestSuite()
    #testunit.addTest(LoginTest("test_login5"))
    #runner = unittest.TextTestRunner()
    #runner.run(testunit)
