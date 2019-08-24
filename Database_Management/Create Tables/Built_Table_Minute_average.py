
### Author: Lihua Pei (Neo)
### lihua.peidata@gmail.edu
### Created at July 2019


## Step 1 import Packages
import pymysql.cursors


## Step 2 connect to the local MySQL database

# Connect to the database

connection = pymysql.connect(host='127.0.0.1',
                             
                             # host = 127.0.0.1 or host = 'localhost'(本地电脑)
                             port= 3306,
                             db = 'your_database_name',
                             user = 'your_username',
                             password = 'your_pasword',
                             cursorclass=pymysql.cursors.DictCursor)


#From our connection we need a cursor, which acts as our interface into the database
cur = connection.cursor()



## 1A minute table:

make_1400001A_Minute_Average_table = '''CREATE TABLE 1400001A_Minute_Average(
    uRAD VARCHAR(255),
    Location VARCHAR(255),
    Time_Str_Min VARCHAR(255),
    Year NUMERIC,
    Month NUMERIC,
    Day NUMERIC,
    Hour NUMERIC,
    Minute NUMERIC,
    Particulate_Matter_PM1 DOUBLE,
    Particulate_Matter_PM25 DOUBLE,
    Particulate_Matter_PM10 DOUBLE,
    Ozone_O3_ppm DOUBLE,
    Nitrogen_Dioxide_NO2_ppm DOUBLE,
    Sulfer_Dioxide_SO2_ppm DOUBLE,
    Carbon_Monoxide_CO_ppm DOUBLE,
    VOC_AQI DOUBLE,
    Temperature DOUBLE,
    Pressure DOUBLE,
    Humidity DOUBLE,
    Noise DOUBLE,
    latitude DOUBLE,
    longitude DOUBLE,
    PRIMARY KEY (Time_Str_Min));'''

cur.execute(make_1400001A_Minute_Average_table)
connection.commit()


## 18 minute table

make_14000018_Minute_Average_table = '''CREATE TABLE 14000018_Minute_Average(
    uRAD VARCHAR(255),
    Location VARCHAR(255),
    Time_Str_Min VARCHAR(255),
    Year NUMERIC,
    Month NUMERIC,
    Day NUMERIC,
    Hour NUMERIC,
    Minute NUMERIC,
    Particulate_Matter_PM1 DOUBLE,
    Particulate_Matter_PM25 DOUBLE,
    Particulate_Matter_PM10 DOUBLE,
    Ozone_O3_ppm DOUBLE,
    Nitrogen_Dioxide_NO2_ppm DOUBLE,
    Sulfer_Dioxide_SO2_ppm DOUBLE,
    Carbon_Monoxide_CO_ppm DOUBLE,
    VOC_AQI DOUBLE,
    Temperature DOUBLE,
    Pressure DOUBLE,
    Humidity DOUBLE,
    Noise DOUBLE,
    latitude DOUBLE,
    longitude DOUBLE,
    PRIMARY KEY (Time_Str_Min));'''

cur.execute(make_14000018_Minute_Average_table)
connection.commit()


## 1C minute table

make_1400001C_Minute_Average_table = '''CREATE TABLE 1400001C_Minute_Average(
    uRAD VARCHAR(255),
    Location VARCHAR(255),
    Time_Str_Min VARCHAR(255),
    Year NUMERIC,
    Month NUMERIC,
    Day NUMERIC,
    Hour NUMERIC,
    Minute NUMERIC,
    Particulate_Matter_PM1 DOUBLE,
    Particulate_Matter_PM25 DOUBLE,
    Particulate_Matter_PM10 DOUBLE,
    Ozone_O3_ppm DOUBLE,
    Nitrogen_Dioxide_NO2_ppm DOUBLE,
    Sulfer_Dioxide_SO2_ppm DOUBLE,
    Carbon_Monoxide_CO_ppm DOUBLE,
    VOC_AQI DOUBLE,
    Temperature DOUBLE,
    Pressure DOUBLE,
    Humidity DOUBLE,
    Noise DOUBLE,
    latitude DOUBLE,
    longitude DOUBLE,
    PRIMARY KEY (Time_Str_Min));'''

cur.execute(make_1400001C_Minute_Average_table)
connection.commit()


## 58 minute table

make_14000058_Minute_Average_table = '''CREATE TABLE 14000058_Minute_Average(
    uRAD VARCHAR(255),
    Location VARCHAR(255),
    Time_Str_Min VARCHAR(255),
    Year NUMERIC,
    Month NUMERIC,
    Day NUMERIC,
    Hour NUMERIC,
    Minute NUMERIC,
    Particulate_Matter_PM1 DOUBLE,
    Particulate_Matter_PM25 DOUBLE,
    Particulate_Matter_PM10 DOUBLE,
    Ozone_O3_ppm DOUBLE,
    Nitrogen_Dioxide_NO2_ppm DOUBLE,
    Sulfer_Dioxide_SO2_ppm DOUBLE,
    Carbon_Monoxide_CO_ppm DOUBLE,
    VOC_AQI DOUBLE,
    Temperature DOUBLE,
    Pressure DOUBLE,
    Humidity DOUBLE,
    Noise DOUBLE,
    latitude DOUBLE,
    longitude DOUBLE,
    PRIMARY KEY (Time_Str_Min));'''

cur.execute(make_14000058_Minute_Average_table)
connection.commit()



## 5A minute table

make_1400005A_Minute_Average_table = '''CREATE TABLE 1400005A_Minute_Average(
    uRAD VARCHAR(255),
    Location VARCHAR(255),
    Time_Str_Min VARCHAR(255),
    Year NUMERIC,
    Month NUMERIC,
    Day NUMERIC,
    Hour NUMERIC,
    Minute NUMERIC,
    Particulate_Matter_PM1 DOUBLE,
    Particulate_Matter_PM25 DOUBLE,
    Particulate_Matter_PM10 DOUBLE,
    Ozone_O3_ppm DOUBLE,
    Nitrogen_Dioxide_NO2_ppm DOUBLE,
    Sulfer_Dioxide_SO2_ppm DOUBLE,
    Carbon_Monoxide_CO_ppm DOUBLE,
    VOC_AQI DOUBLE,
    Temperature DOUBLE,
    Pressure DOUBLE,
    Humidity DOUBLE,
    Noise DOUBLE,
    latitude DOUBLE,
    longitude DOUBLE,
    PRIMARY KEY (Time_Str_Min));'''

cur.execute(make_1400005A_Minute_Average_table)
connection.commit()





