# -*- coding: utf-8 -*-
import  os
import xlrd
class ExcelRead:
    def __init__(self,file_path,file_sheet):
            if os.path.exists(file_path):
                self.file_path = file_path
                self.file_sheet = file_sheet
            else:
                raise  FileNotFoundError("文件不存在")

    def  data(self):
            #创建book对象
            work = xlrd.open_workbook(self.file_path)

            #判断读取方式
            if type(self.file_sheet) not in [int,str]:
                print("读取错误")
            elif type(self.file_sheet) == int:
                sheet = work.sheet_by_index(self.file_sheet)
            elif type(self.file_sheet) == str:
                sheet = work.sheet_by_name(self.file_sheet)

            cols = sheet.ncols
            for i in range(cols):
                c_value = sheet.col_values(i)

            return c_value


if __name__ == '__main__':
    ec =ExcelRead("D:\\Probject_Redmine_01\\data\\user.xlsx","Sheet1").data()

    print(ec[0])