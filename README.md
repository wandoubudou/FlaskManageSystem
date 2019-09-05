# FlaskManageSystem
Flask课设，自学一个礼拜做出的课设作品

我的数据库是mysql, 运行此项目需要导入向mysql中导入数据，并且建立数据表
一个简单的管理系统，供大家学习和参考

## 一些用到的python包: pymysql,flask. 
你可以通过pip命令来下载他们

``` bash
pip install pymysql
pip install flask
```

### 要运行这个程序，首先需要创建数据库
### 1.打开数据库终端，并输入以下命令

``` bash
CREATE DATABASE test1 DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
use test1;
CREATE TABLE staffdetail(Name varchar(50) NOT NULL PRIMARY KEY,Position varchar(80),Office varchar(80),Age INT(10),StartDate varchar(80),Salary varchar(80));
CREATE TABLE account(EmailAddress varchar(50) NOT NULL PRIMARY KEY,FirstName varchar(80),LastName varchar(80),Password varchar(80));
show tables;
```
看到控制台显示两个数据库则创建成功

### 2.在程序 dbutils/config下有一个FLAGS的字典，

修改name和pwd为自己的数据库用户名和密码
你也可以修改一些别的属性，更多的操作等你探索


### 3.导入数据到staffdetail表单中，可以手动导入，也可以运行我写的my_dbscript脚本文件

直接运行即可将默认数据填入staffdetail表单    （推荐）

手动将excel文件导入mysql可以自行上网查看方法



### 4.运行 app.py主文件
看到打印的信息127.0.0.1:5000/ 代表成功运行
用浏览器输入http://127.0.0.1:5000/ 即可查看到做好的网页程序



### 下面是成果展示

![alt text](https://github.com/wandoubudou/FlaskManageSystem/blob/master/images/1.png "index")












![alt text](https://github.com/wandoubudou/FlaskManageSystem/blob/master/images/2.png "index")
