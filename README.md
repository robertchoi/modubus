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


- 참고  
https://hiiambk.tistory.com/368




- 라즈베리파이 보드 버전 확인
cat /proc/device-tree/model


- 참고
https://blog.naver.com/software705/221337666338
https://blusky10.tistory.com/362
https://backkom-blog.tistory.com/entry/Raspberry-Pi%EB%9D%BC%EC%A6%88%EB%B2%A0%EB%A6%AC%ED%8C%8C%EC%9D%B4-Docker-Redmine-Mysql-Git-%EC%84%B8%ED%8C%85%ED%95%98%EA%B8%B0-1%ED%8E%B8-Docker%EB%9E%80-17?category=294180

https://121202.tistory.com/24



- 파이썬에서 사용하기
http://www.hardcopyworld.com/gnuboard5/bbs/board.php?bo_table=lecture_rpi&wr_id=37

https://www.tutorialspoint.com/python/python_database_access.htm

- db 생성
~~~
CREATE DATABASE pidb;
~~~

- db 사용
~~~
USE pidb;
~~~

- 테이블 생성
~~~
CREATE TABLE test (
no int(11) NOT NULL auto_increment,
datef varchar(16) NOT NULL,
timef varchar(16) NOT NULL,
ff varchar(16) NOT NULL,
df varchar(16) NOT NULL,
vf varchar(16) NOT NULL,
cf varchar(16) NOT NULL,
PRIMARY KEY (no)
);
~~~

- 테이블 보기
~~~
SHOW TABLES;
~~~

