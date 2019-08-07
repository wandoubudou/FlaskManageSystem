from dbutils.connection import Conn_mysql

def login_check(EmailAddress,Password):
    conn = Conn_mysql("","",EmailAddress=EmailAddress,Password=Password)
    res = conn.check_account()
    return res
