# -*- coding: utf-8 -*-

from  selenium.webdriver.common.by import By

#登录元素定位操作
class  Longin_Signin:

    username = (By.ID,"username") #登录名

    password = (By.ID,"password") #登录密码

    loginButton = (By.NAME,"login")#登录按钮

    longname = (By.XPATH,"(//a[text()='admin'])[2]")#登录后的名字


#新建用户元素定位操作
class  UserPageLocators:
    #新建用户
    New_user = (By.XPATH,"//a[text()='新建用户']")
    #登录名
    User = (By.XPATH,"//input[@id ='user_login']")
    #用户名
    Nmae = (By.ID,"user_firstname")
    #用户姓
    Ming = (By.ID,"user_lastname")
    #用户邮箱
    Mail = (By.ID,"user_mail")
    #用户密码
    password = (By.ID,"user_password")
    #确认密码
    password1 = (By.ID,("user_password_confirmation"))
    #创建按钮
    commit = (By.NAME,"commit")


#删除用户元素定位操作
class User_Del:
    #搜索输入框
    name = (By.XPATH,"//*[@id='name']")
    #应用按钮
    small = (By.XPATH, '(//input[@class="small"])[2]')
    #删除操作
    dele = (By.XPATH,"//a[text()='删除']")



#新建项目元素定位操作
class Pobject_add:
    #新建项目按钮
    pobject_add = (By.XPATH,"//a[text()='新建项目']")
    #项目名称
    pobject_name = (By.XPATH,"//input[@id='project_name']")
    #确认按钮
    pobJect_commit = (By.NAME,"commit")



#项目删除元素定位
class Pobject_del:
    #搜索框
    pobject_name = (By.XPATH,"//input[@id = 'name']")
    #应用按钮
    pobject_commit = (By.XPATH,"(//input[@class='small'])[2]")

    #点击删除
    pobject_shanchu = (By.XPATH,"//a[text()='删除']")

    #删除勾选
    pobject_checklist  = (By.XPATH,"//input[@id ='confirm']")#//input[@id ='confirm']//input[@id = 'confirm'
    #删除操作
    pobject_del  = (By.XPATH,"//input[@name= 'commit']")


#新建bug缺陷元素定位

class Add_bug:
     #新建问题按钮
     add_name_bug = (By.XPATH,"(//a[text()='新建问题'])[2]")
     #主题
     theme_name = (By.XPATH,"//input[@id = 'issue_subject']")
     #确认按钮
     add_bug_commit = (By.XPATH,"//input[@name = 'commit']")


class Del_bug:
    #搜索
    sear_bug = (By.XPATH,"//input[@id='q']")
    #回车事件
    enter = (By.XPATH,"//input[@id='q']")
    #点击结果
    result_bug = (By.XPATH,'//dl[@id="search-results"]/dt/a')
    #选中删除选项
    bug_shanchu  = (By.XPATH,"(//a[text() ='删除'])[1]")
