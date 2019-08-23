# Remote Linux Database Introduction. 
Author: Lihua Pei (Neo)
2019 Augest 21


## 1. Basic Linux Commend Lines.

#### ls

ls is the list commend which will return the all files under the current diraction.

eg:
```bash
[neo_freshairdc@plato MySQL_Database]$ ls
API_Minute_update.py  Built_Table_Minute_average.py  test.py
```

#### cd

The cd command is used to change the current directory (i.e., the directory in which the user is currently working). 

eg:
```bash
[neo_freshairdc@plato ~]$ ls
Data_Visualization  LR_model  MySQL_Database
[neo_freshairdc@plato ~]$ cd MySQL_Database/      (move to the MySQL_Database file)
[neo_freshairdc@plato MySQL_Database]$ ls
API_Minute_update.py  Built_Table_Minute_average.py  test.py

[neo_freshairdc@plato MySQL_Database]$ cd         (cd with no directory will return to the root)
[neo_freshairdc@plato ~]$ ls
Data_Visualization  LR_model  MySQL_Database
```
## 2. Advanced Linux operations.

#### 1. Transfrom the files from local to server.

scp your_file_directory freshairdc@plato.seas.gwu.edu: the server_store_directory

eg:
```bash
scp /Users/neopei/Desktop/Air_DC/Fresh_Air_DC_Database/Built_Table_Minute_average.py neo_freshairdc@plato.seas.gwu.edu:/home/neo_freshairdc/MySQL_Database

Password: your_password
```

#### 2. Screen.

Screen is a full-screen software program that can be used to multiplexes a physical console between several processes (typically interactive shells). It offers a user to open several separate terminal instances inside a one single terminal window manager.

The screen application is very useful, if you are dealing with multiple programs from a command line interface and for separating programs from the terminal shell. It also allows you to share your sessions with others users and detach/attach terminal sessions.

Check exist screens:
```bash
screen -ls
There is a screen on:
	7066.Neo_uRAD_API	(Multi, detached)
```
7066 is the screen I created to continuely running the code.

re-attach screen:
```bash
screen -r 7066
```
Then use control + A + D to detach the screen.




## 3. Remote operations of Fresh_Air_DC server.

#### 1. 'ssh' remote connection to the server.

```bash
ssh your_account_freshairdc@plato.seas.gwu.edu
password: your_password
```

#### 2. Fresh_Air_DC database connection.
```bash
mysql -u freshairdc -p 
Enter pasword: your_database_password
Welcome to the MariaDB monitor.  Commands end with ; or \g.
MariaDB [(none)]> 
```

```bash
MariaDB [(none)]> use freshairdata;
MariaDB [freshairdata]> show tables;
+-------------------------+
| Tables_in_freshairdata  |
+-------------------------+
| 14000018_Minute_Average |
| 1400001A_Minute_Average |
| 1400001C_Minute_Average |
| 14000058_Minute_Average |
| 1400005A_Minute_Average |
+-------------------------+
```
```bash
select count(*) from 14000058_Minute_Average where Month = 8 AND Day = 19;
+----------+
| count(*) |
+----------+
|     1319 |
+----------+
```
