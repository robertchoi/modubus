# modubus

### modbus pi module
https://minimalmodbus.readthedocs.io/en/master/index.html


### 파이썬 가상환경
~~~
sudo apt-get update
sudo apt-get upgrade

sudo apt-get install build-essential python3 python3-dev python3-pip python3-virtualenv

python3 -m virtualenv -p python3 env --system-site-packages
echo "source env/bin/activate" >> ~/.bashrc
source ~/.bashrc
~~~


### MySql 설치
sudo apt-get install mysql-server mysql-client

### MySql 삭제
sudo apt-get remove mysql-server mysql-client
sudo apt-get autoremove

### MySql 설정
sudo mysql -u root mysql


~~~
(env) pi@raspberrypi:~/modubus $ sudo mysql -u root mysql
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 2
Server version: 10.1.44-MariaDB-0+deb9u1 Raspbian 9.11

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [mysql]> 
~~~  

~~~
MariaDB [mysql]> update user set plugin='';
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

MariaDB [mysql]> update user set password=PASSWORD('12345678') where User='root';
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

MariaDB [mysql]> flush privileges;
Query OK, 0 rows affected (0.00 sec)
~~~


sudo /etc/init.d/mysql stop
sudo /usr/sbin/mysqld



pip install pymysql


- 참고
  
https://hiiambk.tistory.com/368


MariaDB [mysql]> select host, user, password from user;
+-----------+------+----------+
| host      | user | password |
+-----------+------+----------+
| localhost | root | 12345678 |
+-----------+------+----------+
1 row in set (0.00 sec)


- 라즈베리파이 보드 버전 확인
  
cat /proc/device-tree/model