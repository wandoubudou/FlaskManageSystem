from utils.manage_staff.admin_change import change_info

def temp():
    print("增 : insert\n改 : update\n删 : delete   q for quit")
    cmd = input("请输入您需要的操作\n")
    if cmd=="insert":
        data = input("please input Name, Position, Office, Age, StartDate, Salary\n").split()
        db_change = change_info(data[0],data[1],data[2],data[3],data[4],data[5])
        res = db_change.insert_staff()
        print(res)
        temp()
    if cmd=="update":
        data = input("please input Name, Position, Office, Age, StartDate, Salary\n").split()
        db_change = change_info(data[0],data[1],data[2],data[3],data[4],data[5])
        res = db_change.update_staff()
        print(res)
        temp()
    if cmd=="delete":
        data = input("please input the person Name who you want to delete ... \n")
        db_change = change_info(data," "," "," "," "," ")
        res = db_change.delete_staff()
        print(res)
        temp()
    if cmd == 'q':
        return
temp()
