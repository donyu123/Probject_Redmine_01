# -*- coding: utf-8 -*-
from  selenium import  webdriver
import time
from config.Config import ReadMe
from  page.reamine_page import *
from utils.LogginUtils import my_log
from common.redmine_login import RedmineLogin
import pytest

#获取url
add_pobject_url = ReadMe("D:\\Probject_Redmine_01\\config\\ReadMe.ini").ip_address()

#获取时间戳
time_add_bug = "selebug{}".format(time.time())

class Test_add_bug:
    pass
    #问题 #1 已创建。
    #实例化对象
    def setup_class(self):
         self.driver = RedmineLogin().log_redmine()
         self.driver.get("http://{}/redmine/projects/s1/issues".format(add_pobject_url))

    def test_add_bug(self):
        addbug = Add_Bug_page(self.driver)
        #新建问题
        addbug.add_bug()
        #输入新建标题
        addbug.add_name_bug(time_add_bug)
        #新建缺陷
        addbug.add_bug_commit()
        #校验
        assert "已创建" in self.driver.page_source
        time.sleep(3)

    def teardown_class(self):
        #地址
        self.driver.get("http://{}/redmine/projects/s1/issues".format(add_pobject_url))
        #实例化
        del_bug_page = Del_Bug_page(self.driver)
        #搜索bug名称
        del_bug_page.del_bug_shanchu(time_add_bug)
        #回车事件
        del_bug_page.enert()
        time.sleep(3)
        #点击搜索结果
        del_bug_page.result()
        #点击删除
        del_bug_page.bug_shanchuU()
        time.sleep(3)
        #确定弹窗
        self.driver.switch_to.alert.accept()
        time.sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(["-s","test_0004_add_bug.py"])