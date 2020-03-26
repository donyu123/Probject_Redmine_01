# -*- coding: utf-8 -*-
from  page.readmine_locators import *
from selenium.webdriver.common.keys import Keys
class BasePage():
    def __init__(self,driver):
        self.driver = driver

#用户登录页面元素的操作
class LogPage(BasePage):

    #用户名
    def login_name(self,name):
        ele = self.driver.find_element(*Longin_Signin.username)
        ele.send_keys(name)

    #用户密码
    def login_password(self):
        ele = self.driver.find_element(*Longin_Signin.password)
        ele.send_keys("dy1994522")

    #点击登录
    def login_click_button(self):
        ele = self.driver.find_element(*Longin_Signin.loginButton)
        ele.click()

    #验证是否登录成功
    def get_login_name(self):
        ele =self.driver.find_element(*Longin_Signin.longname)
        return ele.text

#创建用户
class User_New(BasePage):

    # 新建用户
    def New_user(self):
        ele = self.driver.find_element(*UserPageLocators.New_user).click()

    #登录名
    def  user(self,user):
        ele = self.driver.find_element(*UserPageLocators.User)
        ele.send_keys(user)

    #姓
    def name(self):
        ele = self.driver.find_element(*UserPageLocators.Nmae)
        ele.send_keys('a')
    #名
    def  ming(self):
        ele = self.driver.find_element(*UserPageLocators.Ming)
        ele.send_keys('b')

    #邮箱
    def mail(self,email):
        ele = self.driver.find_element(*UserPageLocators.Mail)
        ele.send_keys(email)
    #用户密码
    def password(self):
        ele = self.driver.find_element(*UserPageLocators.password)
        ele.send_keys("12345678")

    #确认密码
    def password1(self):
        ele = self.driver.find_element(*UserPageLocators.password1)
        ele.send_keys("12345678")
    #点击新建
    def commit(self):
        ele = self.driver.find_element(*UserPageLocators.commit)
        ele.click()

#删除用户
class Del_User(BasePage):

    #搜索框
    def search_name(self,name):
        ele = self.driver.find_element(*User_Del.name)
        ele.send_keys(name)

    #应用搜索按钮
    def application_small(self):
        ele = self.driver.find_element(*User_Del.small)
        ele.click()

    #删除操作
    def  dele(self):
        ele = self.driver.find_element(*User_Del.dele)
        ele.click()


#新建项目
class Pobject_add_page(BasePage):
    #创建项目
    def add_pobject(self):
        ele = self.driver.find_element(*Pobject_add.pobject_add)
        ele.click()


    #输入项目名称
    def add_name_page(self,add_name):
        ele = self.driver.find_element(*Pobject_add.pobject_name)
        ele.send_keys(add_name)

    #确定创建
    def commit_page(self):
        ele = self.driver.find_element(*Pobject_add.pobJect_commit)
        ele.click()

#删除项目
class  Pobject_del_page(BasePage):

    #搜索框输入搜索内容
    def pobject_del_name(self,del_name):
        ele = self.driver.find_element(*Pobject_del.pobject_name)
        ele.send_keys(del_name)

    #搜索内容应用按钮
    def pobject_del_commit(self):
        ele = self.driver.find_element(*Pobject_del.pobject_commit)
        ele.click()
    #点击删除
    def pobject_del_shanchu(self):
        ele = self.driver.find_element(*Pobject_del.pobject_shanchu)
        ele.click()

    #勾选是否删除
    def pobject_del_checklist(self):
        ele = self.driver.find_element(*Pobject_del.pobject_checklist)
        ele.click()

    #删除按钮
    def pobject_del(self):
        ele = self.driver.find_element(*Pobject_del.pobject_del)
        ele.click()


#创建缺陷
class  Add_Bug_page(BasePage):
    #新建问题
    def add_bug(self):
        ele = self.driver.find_element(*Add_bug.add_name_bug)
        ele.click()

    #输入新建信息名称
    def add_name_bug(self,add_theme_name):
        ele =self.driver.find_element(*Add_bug.theme_name)
        ele.send_keys(add_theme_name)
    #新建按钮
    def add_bug_commit(self):
        ele = self.driver.find_element(*Add_bug.add_bug_commit)
        ele.click()

#删除操作
class Del_Bug_page(BasePage):

    #选中删除选项
    def del_bug_shanchu(self,add_theme_name):
        ele = self.driver.find_element(*Del_bug.sear_bug)
        ele.send_keys(add_theme_name)

    #回车事件
    def enert(self):
        ele =  self.driver.find_element(*Del_bug.enter)
        ele.send_keys(Keys.ENTER)

    #点击结果事件
    def result(self):
        ele = self.driver.find_element(*Del_bug.result_bug)
        ele.click()

    #删除bug
    def bug_shanchuU(self):
        ele = self.driver.find_element(*Del_bug.bug_shanchu)
        ele.click()
