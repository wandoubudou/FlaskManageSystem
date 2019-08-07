from dbutils.connection import Conn_mysql

def reset_pwd(EmailAddress,Password):
    conn = Conn_mysql("", "", EmailAddress=EmailAddress, Password=Password)
    res = conn.reset_password()
    if res=="Success...":
        return "Success..."
    else:
        return res

