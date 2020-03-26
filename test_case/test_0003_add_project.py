# -*- coding: utf-8 -*-
from  common.redmine_login import RedmineLogin
from  config.Config import ReadMe
from page.reamine_page import *
import  time
import pytest
from utils.allureUtils import allure_test


#获取url
add_pobject_url = ReadMe("D:\\Probject_Redmine_01\\config\\ReadMe.ini").ip_address()

#获取时间戳
time_pobject = "sele{}".format(time.time())

class  Test_Pobject_add:

    #初始化方法登录
    def  setup_class(self):
        self.driver =  RedmineLogin().log_redmine()
        self.driver.get("http://{}/redmine/projects".format(add_pobject_url))

    #新建项目
    def test_pobject_add(self):
        """
        实例化对象
        调用新建按钮
        调用输入项目名称
        调用确定按钮
        判断是否创建成功
        http://192.168.1.225:81/redmine/projects
        :return:
        """

        pobj_add = Pobject_add_page(self.driver)
        time.sleep(2)

        pobj_add.add_pobject()
        time.sleep(2)

        pobj_add.add_name_page(time_pobject)
        time.sleep(2)

        pobj_add.commit_page()
        time.sleep(2)

        assert '创建成功' in self.driver.page_source
        time.sleep(2)



    def  teardown_class(self):
         #获取管理项目地址
         #实例化对象
         #输入项目名称
         #确定应用搜索按钮
         #点击删除
         #是否删除勾选
         #删除
        self.driver.get("http://{}/redmine/admin/projects".format(add_pobject_url))

        pobj_del_page = Pobject_del_page(self.driver)
        time.sleep(2)

        pobj_del_page.pobject_del_name(time_pobject)
        time.sleep(2)

        pobj_del_page.pobject_del_commit()
        time.sleep(2)

        pobj_del_page.pobject_del_shanchu()

        pobj_del_page.pobject_del_checklist()
        time.sleep(2)

        pobj_del_page.pobject_del()
        time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(["-s","test_0003_add_project.py"])