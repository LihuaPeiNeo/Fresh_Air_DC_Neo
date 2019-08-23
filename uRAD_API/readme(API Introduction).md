# uRAD API Introduction
Author: Lihua Pei (Neo)
2019 Augest 14


## 1. uRAD API Introduction.

uRAD Monitor provide the api to request data for the user. 

This is the  detailed  [uRAD_Monitor_API_Introduction](https://github.com/LihuaPeiNeo/Fresh_Air_DC_neo/tree/master/uRAD_API/code_file/uradmonitor_API.pdf) documention.

1. We need to open the terminal.
2. Type the commend lines: 

```bash
curl -H "X-User-id: your_user_id" -H "X-User-hash: your_password" https://data.uradmonitor.com/api/v1/devices/[monitor_id]/[features]/[start_time]/[end_time]
```

eg: to quary the all features of monitor 1400005A

```bash
curl -H "X-User-id: your_user_id" -H "X-User-hash: your_password" https://data.uradmonitor.com/api/v1/devices/1400005A/all
```

This quary will return the lastest 24 hours data and the data form is json like dictionary. we take the last one set of the data of our query will be the last measurement of monitor 1400005A updated. 

The data looks like:

```bash
{"time":1565992426,"latitude":38.900100000000002,"longitude":-77.047899999999998,"altitude":-3.5,"timelocal":2527680,"temperature":32.5,"pressure":101422,"humidity":55.190000000000005,"voc":327419.35999999999,"vocaqi":0,"noise":41.319999999999993,"pm1":0,"pm25":3,"pm10":4,"gas1":0.10000000000000001,"gas2":0.062,"gas3":0.14499999999999999,"gas4":1.1140000000000001}
```

"time" : encoded timestamp.
"pm1" : Particulate Matter (PM1) (ug/mÂ³)
"pm25" : Particulate Matter (PM2.5) (ug/mÂ³)
"pm10" : Particulate Matter (PM10) (ug/mÂ³)
"gas1" : Ozone (O3) (ppm)
"gas2" : Nitrogen Dioxide (NO2) (ppm)
"gas3" : Sulfer Dioxide (SO2) (ppm)
"gas4" : Carbon Monoxide (CO) (ppm)




## 2. uRAD_Monitor_API quary data by Python.

Please check the source code [uRAD_API_Insert.py](cod_file\uRAD_API_Insert.py) for more detailed uRAD_API request, data preprocessing and database insert. 

#### 1. Import the python packages.

```python
import pymysql.cursors
import time
import pandas as pd
import numpy as np
import requests
```
<strong>pymysql</strong> works with MySQL 5.5+ and MariaDB 5.5+. MySQL is a leading open source database management system. It is a multiuser, multithreaded database management system.
<strong>time</strong> can help us decode the timestep to time string and can help us build a clock which allow us request data from uRAD every 20 second.
<strong>pandas, numpy</strong> the data analytics packages of Python.
<strong>request</strong> allow us to run the commend lines by python (very important).


#### 2. Preprocessing the data
We only to decode the timestamp to the Time_String(str), year(int), month(int), day(int), hour(int), and minute(int).

```python
 def Preprocessing_uRAD_API_min(_time):
    # decode timestamp to time_local.
    time_local = time.localtime(_time)
    
    #decode time_local to time_string and time_struct.
    time_string = time.strftime("%Y-%m-%d %H:%M", time_local) 
    time_struct = time.struct_time(time_local)

    #Break the time_struct to year, month, day, hour, and minute.
    time_year = time_struct[0]
    time_month = time_struct[1]
    time_day = time_struct[2]
    time_hour = time_struct[3]
    time_minute = time_struct[4]
    
    # store data in a list and return this list
    time_list= [time_string, time_year, time_month, time_day, time_hour, time_minute]
    return time_list
```

#### 3. uRAD_ API Request
```python
def API_New_Data(API_string):
        # set up API_header with your id and password
        API_header = {"X-User-id": 'your_user_id', "X-User-hash":"your_password"}
        r= requests.get(API_string, headers=API_header)
        r= r.json()
        #take the last one dataset
        new_API_data = r[-1]
        #use the preprocessing function to decode the timestamp.
        _time = new_API_data.get('time')
        time_list = Preprocessing_uRAD_API_min(_time)
        # add the time list to the dataset and return the formed dataset.
        new_API_data.update({'Time_Str': time_list[0],'Year':time_list[1],'Month':time_list[2],'Day':time_list[3],'Hour':time_list[4],'minute':time_list[5]})
        return new_API_data
# Call the function and enter 'https://data.uradmonitor.com/api/v1/devices/[moniotr_id]/[features]/' to quary the data.
new_5A_data = API_New_Data('https://data.uradmonitor.com/api/v1/devices/1400005A/all/')
```
The new formed data looks like:

```bash
{'time': 1565996926,'latitude': 38.9001,'longitude': -77.0479,'altitude': -1.67,'timelocal': 2532180,
 'temperature': 30.23,'pressure': 101400,'humidity': 61.580000000000005,voc': 327419.36,'vocaqi': 0,
 'noise': 44.010000000000005,'pm1': 0,'pm25': 3,'pm10': 4,
 'gas1': 0.1,'gas2': 0.199,'gas3': 0.143,'gas4': 0.647,
 'Time_Str': '2019-08-16 19:08','Year': 2019,'Month': 8,'Day': 16,'Hour': 19,'minute': 8}
```

