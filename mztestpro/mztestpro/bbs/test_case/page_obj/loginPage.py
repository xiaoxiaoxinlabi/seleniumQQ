#coding:utf-8

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class Login(Page):
    
    login_username_loc = (By.ID, "u")
    login_password_loc = (By.ID, "p")
    login_button_loc = (By.ID, "login_button")
    user_error_hint_loc = (By.XPATH, "//*[@id='login']/div[2]")
    password_error_hint_loc = (By.XPATH, "//*[@id='login']/div[2]")
    user_login_success_loc = (By.XPATH, '//*[@id="useralias"]')
    user_login_frame_loc = "login_frame"
    
    
    def login_username(self, username):
   
        self.find_element(*self.login_username_loc).send_keys(username)

    def login_password(self, password):

        self.find_element(*self.login_password_loc).send_keys(password)

    def login_button(self):

        self.find_element(*self.login_button_loc).click()

    def user_login(self, username = "", password = ""):
        self.open()
       # print("frame_loc=",type(self.user_login_frame_loc),type("login_frame"))
        self.switch_frame(self.user_login_frame_loc)
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(1)

    #用户名错误提示
    def user_error_hint(self):
        return self.find_element(*self.user_error_hint_loc).text

    #密码错误提示
    def password_error_hint(self):
        return self.find_element(*self.password_error_hint_loc).text

    #登录成功用户名
    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text
