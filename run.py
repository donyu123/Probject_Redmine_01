# -*- coding: utf-8 -*-
import pytest
if __name__ == '__main__':
    # 日志报告json文件123
    report_path = "D:\\Probject_Redmine_01\\report\\result"
    # 日志报告
    report_path_html = "D:\\Probject_Redmine_01\\report\\result\\html"
    # 执行请求 并且生成报告json文件
    pytest.main(["-s", "--alluredir", report_path])