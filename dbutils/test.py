import pymysql
from dbutils.config.cfg import *

db = pymysql.connect(FLAGS["local_host"], FLAGS["name"], FLAGS["pwd"], FLAGS["table_name"], charset=FLAGS["charset"])
select_sql = "update account set Password=%s where EmailAddress=%s"
password = "bbm"
EmailAddress = "aaaa@qq.com"
cursor = db.cursor()
data = cursor.execute(select_sql, (password,EmailAddress))

print(data)
db.commit()
db.close()
cursor.close()