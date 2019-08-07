import pymysql
from dbutils.config.cfg import *

class Conn_mysql:
    def __init__(self,FirstName,LastName,EmailAddress,Password):
        self.FirstName = FirstName
        self.LastName = LastName
        self.EmailAddress = EmailAddress
        self.Password = Password
    def check_email(self):
        """检查email是否重复  email可用返回1  不可用返回0"""
        db = pymysql.connect(FLAGS["local_host"],FLAGS["name"], FLAGS["pwd"], FLAGS["table_name"], charset=FLAGS["charset"])
        select_sql = "select * from account where EmailAddress=%s"
        cursor = db.cursor()
        data = cursor.execute(select_sql,(self.EmailAddress))
        print(data)

        db.close()
        if data >= 1:       #查到了
            return False
        elif data==0:       #没查到
            return True


    def register_cmd(self):       #插入注册人信息
        if self.check_email():
            db = pymysql.connect(FLAGS["local_host"], FLAGS["name"], FLAGS["pwd"], FLAGS["table_name"],
                                 charset=FLAGS["charset"])

            insert_sql ="insert into account(FirstName,LastName,EmailAddress,Password) VALUES (%s,%s,%s,%s)"
            cursor = db.cursor()
            temp_data  = cursor.execute(insert_sql,(self.FirstName,self.LastName,self.EmailAddress,self.Password))
            print("temp data = ", temp_data)
            db.commit()
            db.close()
            cursor.close()
            return "Register Success..."
        else:
            return "email address has been used..."

    def check_account(self):
        """ 检查登陆时的账号信息，如果邮箱地址不存在，
            返回邮箱未被注册, 如果密码对不上
            ，返回密码错误， 如果都正确返回Success..."""
        db = pymysql.connect(FLAGS["local_host"], FLAGS["name"], FLAGS["pwd"], FLAGS["table_name"],
                             charset=FLAGS["charset"])
        select_sql = "select * from account where EmailAddress=%s"
        cursor = db.cursor()
        record_number = cursor.execute(select_sql,(self.EmailAddress))
        data = cursor.fetchall()
        if record_number != 0:
            db_pwd = data[0][-1]
            if self.Password==db_pwd:
                return "Success..."
            else:
                return "Wrong Password , please check your password..."
        else:
            return "Email Address is not exist , do you want to use it to register ? "

    def reset_password(self):
        """
        重置密码，如果邮箱存在，重置其密码
                    如果邮箱不存在，返回邮箱不存在，是否要创建新账号？
        """
        if self.check_email()==True:
            return "EmailAddress is not exist , want to creat one ? "
        else:
            db = pymysql.connect(FLAGS["local_host"], FLAGS["name"], FLAGS["pwd"], FLAGS["table_name"],
                                 charset=FLAGS["charset"])
            update_sql = "update account set Password=%s where EmailAddress=%s"
            cursor = db.cursor()
            change_number = cursor.execute(update_sql, (self.Password,self.EmailAddress))
            db.commit()

            db.close()
            cursor.close()
            return "Success..."
