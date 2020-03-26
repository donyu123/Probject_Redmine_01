# -*- coding: utf-8 -*-
import pytest
import  time
from  page.reamine_page import *
from  config.Config import ReadMe
from common.redmine_login import RedmineLogin
from utils.allureUtils import allure_test

time_user= 'user{}'.format(time.time())
re_url= ReadMe("D:\\Probject_Redmine_01\\config\\ReadMe.ini").ip_address()
class Test_User:


    def setup_class(self):
        self.driver = RedmineLogin().log_redmine()
        self.driver.get("http://{}/redmine/users".format(re_url))

    def test_uesr(self):
        """
        创建用户
        创建用户按钮
        用户名字
        用户姓
        用户名
        邮箱132132132
        用户密码
        确认用户密码
        确认创建按钮
        :return:
        """
        user = User_New(self.driver)

        user.New_user()

        user.user(time_user)

        user.name()

        user.ming()

        user.mail("{}@qq.com".format(time_user))

        user.password()

        user.password1()

        user.commit()
        assert "已创建" in self.driver.page_source




    def teardown_class(self):
        self.driver.get("http://{}/redmine/users".format(re_url))
        #实例化
        user_del = Del_User(self.driver)
        #搜索用户
        user_del.search_name(time_user)
        time.sleep(3)
        #确认搜素
        user_del.application_small()
        time.sleep(3)
        #删除用户
        user_del.dele()
        time.sleep(3)
        #确定弹窗
        self.driver.switch_to.alert.accept()
        time.sleep(3)
        self.driver.quit()  

if __name__ == '__main__':
    pytest.main(["-s","test_0002_add_user.py"])