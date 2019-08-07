"""
这是一个修改脚本，只有管理员才可以修改数据库
管理员通过员工名字，找到对应员工，并修改
"""

import pymysql
from dbutils.config.cfg import *

class change_info:
    def __init__(self,Name,Position,Office,Age,StartDate,Salary):
        self.Name = Name
        self.Position = Position
        self.Office = Office
        self.Age = Age
        self.StartDate = StartDate
        self.Salary = Salary

    def check_staff_exist(self):
        """
            查询  staff 姓名 是否已经存在，
            若存在返回True
            若不存在返回False
        """
        db = pymysql.connect(FLAGS["local_host"], FLAGS["name"], FLAGS["pwd"], FLAGS["table_name"],
                             charset=FLAGS["charset"])
        select_sql = "select * from staffdetail where Name = %s"
        cursor = db.cursor()
        temp_data = cursor.execute(select_sql,self.Name)
        if temp_data >= 1:
            return True
        else:
            return False

    def insert_staff(self):
        if self.check_staff_exist()==True:
            return "Staff name has already exist... please check it out ... \n\n"
        else:
            db = pymysql.connect(FLAGS["local_host"], FLAGS["name"], FLAGS["pwd"], FLAGS["table_name"],
                                 charset=FLAGS["charset"])
            insert_sql = "insert into staffdetail(Name,Position,Office,Age,StartDate,Salary) VALUES (%s,%s,%s,%s,%s,%s)"
            cursor = db.cursor()
            temp_data = cursor.execute(insert_sql, (self.Name, self.Position, self.Office, self.Age,self.StartDate,self.Salary))
            db.commit()
            db.close()
            cursor.close()
            return "Success...\n\n"

    def update_staff(self):
        if self.check_staff_exist()==True:
            db = pymysql.connect(FLAGS["local_host"], FLAGS["name"], FLAGS["pwd"], FLAGS["table_name"],
                                 charset=FLAGS["charset"])
            select_sql = "update staffdetail set Position=%s,Office=%s,Age=%s,StartDate=%s,Salary=%s  where Name=%s"
            cursor = db.cursor()
            temp_data = cursor.execute(select_sql,(self.Position, self.Office, self.Age,self.StartDate,self.Salary,self.Name))
            print(temp_data)
            db.commit()
            db.close()
            cursor.close()
            return "Success...\n\n"
        else:
            return "Can't find the person who is called %s\n\n" % self.Name

    def delete_staff(self):
        if self.check_staff_exist()==True:
            db = pymysql.connect(FLAGS["local_host"], FLAGS["name"], FLAGS["pwd"], FLAGS["table_name"],
                                 charset=FLAGS["charset"])
            delete_sql = "delete from staffdetail where Name=%s"
            cursor = db.cursor()
            temp_data = cursor.execute(delete_sql,(self.Name))
            db.commit()
            db.close()
            cursor.close()
            return "Delete Success...\n\n"
        else:
            return "Can't find the person who is called %s\n\n" % self.Name


