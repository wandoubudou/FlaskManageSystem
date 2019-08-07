import pymysql
from dbutils.config.cfg import *
l = []
def get_staff_detail():
    """获取数据库中staffdetail所有信息，并返回一个list（tuple，tuple....tuple）"""
    l = []
    db = pymysql.connect(FLAGS["local_host"], FLAGS["name"], FLAGS["pwd"], FLAGS["table_name"],
                                     charset=FLAGS["charset"])

    show_sql ="select * from staffdetail"
    cursor = db.cursor()

    data = cursor.execute(show_sql)
    for i in cursor.fetchall():
        l.append(i)

    return l

