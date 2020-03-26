# -*- coding: utf-8 -*-
import  allure

def allure_test(class_nane,class_Method,title):
    allure.dynamic.feature(class_nane)
    allure.dynamic.story(class_Method)
    allure.dynamic.title(title)
    # desc = "<font color = 'red'>请求的url:{}</font></Br>" \
    #        "<font color = 'red'>请求类:{}</font></Br>" \
    #        "<font color = 'red'>请求方法:{}</font></Br>" \
    #        "<font color = 'red'>请求结果:{}</font></Br>".format(class_nane,class_Method,url,clasee_Success)
    # allure.dynamic.description(desc)


