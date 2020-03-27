# -*- coding: utf-8 -*-
from  selenium import webdriver
import  time
from page.reamine_page import  *
from utils.ExcelUtils import ExcelRead
from utils.allureUtils import allure_test
from  config.Config import ReadMe

re_url= ReadMe("D:\\Probject_Redmine_01\\config\\ReadMe.ini").ip_address()

url  ="http:{}/redmine/login".format(re_url)
print(url)

excel = ExcelRead("D:\\Probject_Redmine_01\\data\\user.xlsx","Sheet1").data()

class  RedmineLogin:
    @staticmethod
    def  log_redmine():
        driver =  webdriver.Chrome()

        driver.implicitly_wait(10)
        driver.get(url)
        #传入driver 驱动
        loginpage = LogPage(driver)
        #读取excel的用户
        loginpage.login_name(excel[0])
        #输入密码
        loginpage.login_password()
        #确定按钮
        loginpage.login_click_button()
        time.sleep(3)
        return  driver
if __name__ == '__main__':
    RedmineLogin().log_redmine()
    # D:\python\Scripts\pip
    # install - r
    # requirements.txt

    # D:\python\python
    # run.py