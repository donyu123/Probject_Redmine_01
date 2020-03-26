# -*- coding: utf-8 -*-
from configparser import ConfigParser
from  selenium import webdriver
import  time
class  ReadMe:
    def __init__(self,readme):
        self.cfg = ConfigParser()
        if self.cfg.read(readme):
            self.cfg.sections()
        else:
            raise  FileNotFoundError("文件不存在 打开失败")

    #获取ip
    def ip_address(self):
        return self.cfg.get('ip_address','ip')

    #获取用户名
    def user(self):
        return self.cfg.get('user','name')

# if __name__ == '__main__':
#     we = webdriver.Chrome()
#     re= ReadMe("D:\\Probject_Redmine_01\\config\\ReadMe.ini").ip_address()
#     we.get("http://{}/redmine/login".format(re))
#     time.sleep(5)
#     we.quit()

    # print(ReadMe().user())