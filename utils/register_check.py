from dbutils.connection import Conn_mysql

def check(FirstName,LastName,EmailAddress,Password,ConfirmPassword):

    if Password==ConfirmPassword:
        conn = Conn_mysql(FirstName, LastName, EmailAddress, Password)
        res = conn.register_cmd()
        return res
    elif Password!=ConfirmPassword:
        return 'Password and confirm password is not same, please check it out'


