# FlaskManageSystem
Flask课设，自学一个礼拜做出的课设作品

## 我的数据库是mysql, 运行此项目需要导入向mysql中导入数据，并且建立数据表
一个简单的管理系统，供大家学习和参考



# 要运行这个程序，首先需要创建数据库
# 打开数据库终端，并输入以下命令

``` bash
CREATE DATABASE test1 DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
use test1;
CREATE TABLE staffdetail(Name varchar(50) NOT NULL PRIMARY KEY,Position varchar(80),Office varchar(80),Age INT(10),StartDate varchar(80),Salary varchar(80));
CREATE TABLE account(EmailAddress varchar(50) NOT NULL PRIMARY KEY,FirstName varchar(80),LastName varchar(80),Password varchar(80));
show tables;
```



## 下面是成果展示

![alt text](https://github.com/wandoubudou/FlaskManageSystem/blob/master/images/1.png "index")












![alt text](https://github.com/wandoubudou/FlaskManageSystem/blob/master/images/2.png "index")
