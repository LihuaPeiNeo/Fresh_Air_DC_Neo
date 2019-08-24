
### Author: Lihua Pei (Neo)
### Email: lihua.peidata@gmail.edu
### Created at July 2019




#### Step 1 import Packages ######################################################################################################################################

import pymysql.cursors
import time
import pandas as pd
import numpy as np
import requests

#### Step 2 setup functions ##################################################################################################################################

# Function 1: a timer set every 20s send a request by uRAD API
def sleeptime(hour, minute, sec):
    return hour*3600 + minute*60 + sec
second = sleeptime(0,0,20)

# Function 2: Preprocess data decode time value to time_string

def Preprocessing_uRAD_API_min(_time):
    
  
    time_local = time.localtime(_time)
    time_string = time.strftime("%Y-%m-%d %H:%M", time_local) 
    time_struct = time.struct_time(time_local)

    time_year = time_struct[0]
    time_month = time_struct[1]
    time_day = time_struct[2]
    time_hour = time_struct[3]
    time_minute = time_struct[4]
    
    time_list= [time_string, time_year, time_month, time_day, time_hour, time_minute]
        
    
    return time_list

# Function 3： MySQL insert function

class Minute_1A_SQL_Writer_API_updating_one():
    def __init__(self,df, cursor, connection):
        self.cursor = cursor
        self.conn = connection

        """Load data from JSON object
        Args:
            user (dict) - json of object
        """
        
        self.uRAD = '1400001A'
        self.location = 'River Terrace'
        
        self.Time_Str_Minute = df.get('Time_Str',None)
        self.Year = int(df.get('Year', None))
        self.Month = int(df.get('Month', None))
        self.Day = int(df.get('Day', None))
        self.Hour = int(df.get('Hour',None))
        self.Minute = int(df.get('minute',None))
        
        self.Particulate_Matter_PM1 = df.get('pm1', None)
        self.Particulate_Matter_PM25 = df.get('pm25', None)
        self.Particulate_Matter_PM10 = df.get('pm10', None)
        self.Ozone_O3_ppm = df.get('gas1',None)
        self.Nitrogen_Dioxide_NO2_ppm = df.get('gas2',None)
        self.Sulfer_Dioxide_SO2_ppm = df.get('gas3', None)
        self.Carbon_Monoxide_CO_ppm = df.get('gas4', None)
        self.VOC = df.get('vocaqi',None)
        self.Temperature = df.get('temperature', None)
        self.Pressure = df.get('pressure', None)
        self.Humidity = df.get('humidity', None)
        self.Noise = df.get('noise',None)
        self.latitude = df.get('latitude', None)
        self.longitude = df.get('longitude',None)
        
        try:
            self.Particulate_Matter_PM1 = float(self.Particulate_Matter_PM1)
        except:
            pass
        try:
            self.VOC = float(self.VOC)
        except:
            pass
        
        try:
            self.Particulate_Matter_PM25 = float(self.Particulate_Matter_PM25)
        except:
            pass
        try:
            self.Particulate_Matter_PM10 = float(self.Particulate_Matter_PM10)
        except:
            pass
        try:
            self.Ozone_O3_ppm = float(self.Ozone_O3_ppm)
        except:
            pass
        try:
            self.Nitrogen_Dioxide_NO2_ppm = float(self.Nitrogen_Dioxide_NO2_ppm)
        except:
            pass
        try:
            self.Sulfer_Dioxide_SO2_ppm = float(self.Sulfer_Dioxide_SO2_ppm)
        except:
            pass
        try:
            self.Carbon_Monoxide_CO_ppm = float(self.Carbon_Monoxide_CO_ppm)
        except:
            pass
        try:
            self.Temperature = float(self.Temperature)
        except:
            pass
        try:
            self.Pressure = float(self.Pressure)
        except:
            pass
        try:
            self.Humidity = float(self.Humidity)
        except:
            pass
        try:
            self.Noise = float(self.Noise)
        except:
            pass
        try:
            self.latitude = float(self.latitude)
        except:
            pass
        try:
            self.longitude = float(self.longitude)
        except:
            pass
        
        
    def insert(self):
        """Inserts a list of objects into the given connection
        Args:
            objs (list) - list of SQL helper objects
        """
        try:
             
            self.cursor.execute(self.get_insert_query(), self.get_values())
        except Exception as e:
            print(e)
            
        self.conn.commit()

    def get_values(self):
        """Get the values used for inseritng a SQL record
        Returns:
            tuple - tuple in ordered format for SQL table
        """
        values = (self.uRAD,self.location, self.Time_Str_Minute, self.Year,self.Month,
                  self.Day, self.Hour, self.Minute, self.Particulate_Matter_PM1, self.Particulate_Matter_PM25,
                  self.Particulate_Matter_PM10,
                  self.Ozone_O3_ppm, self.Nitrogen_Dioxide_NO2_ppm, self.Sulfer_Dioxide_SO2_ppm, 
                  self.Carbon_Monoxide_CO_ppm,self.VOC,self.Temperature,self.Pressure,self.Humidity,self.Noise,self.latitude,self.longitude)

        return values

    def get_insert_query(self):
        """Get the string SQL insert statement
        Returns:
            str - insert statement
        """
        _insert = f"""INSERT INTO 1400001A_Minute_Average VALUES (%s,%s, %s, %s, %s,%s,%s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        return _insert

    

class Minute_18_SQL_Writer_API_updating_one():
    def __init__(self,df, cursor, connection):
        self.cursor = cursor
        self.conn = connection

        """Load data from JSON object
        Args:
            user (dict) - json of object
        """
        
        self.uRAD = '14000018'
        self.location = 'River Terrace'
        
        self.Time_Str_Minute = df.get('Time_Str',None)
        self.Year = int(df.get('Year', None))
        self.Month = int(df.get('Month', None))
        self.Day = int(df.get('Day', None))
        self.Hour = int(df.get('Hour',None))
        self.Minute = int(df.get('minute',None))
        
        self.Particulate_Matter_PM1 = df.get('pm1', None)
        self.Particulate_Matter_PM25 = df.get('pm25', None)
        self.Particulate_Matter_PM10 = df.get('pm10', None)
        self.Ozone_O3_ppm = df.get('gas1',None)
        self.Nitrogen_Dioxide_NO2_ppm = df.get('gas2',None)
        self.Sulfer_Dioxide_SO2_ppm = df.get('gas3', None)
        self.Carbon_Monoxide_CO_ppm = df.get('gas4', None)
        self.VOC = df.get('vocaqi',None)
        self.Temperature = df.get('temperature', None)
        self.Pressure = df.get('pressure', None)
        self.Humidity = df.get('humidity', None)
        self.Noise = df.get('noise',None)
        self.latitude = df.get('latitude', None)
        self.longitude = df.get('longitude',None)
        
        try:
            self.Particulate_Matter_PM1 = float(self.Particulate_Matter_PM1)
        except:
            pass
        
        try:
            self.VOC = float(self.VOC)
        except:
            pass
        try:
            self.Particulate_Matter_PM25 = float(self.Particulate_Matter_PM25)
        except:
            pass
        try:
            self.Particulate_Matter_PM10 = float(self.Particulate_Matter_PM10)
        except:
            pass
        try:
            self.Ozone_O3_ppm = float(self.Ozone_O3_ppm)
        except:
            pass
        try:
            self.Nitrogen_Dioxide_NO2_ppm = float(self.Nitrogen_Dioxide_NO2_ppm)
        except:
            pass
        try:
            self.Sulfer_Dioxide_SO2_ppm = float(self.Sulfer_Dioxide_SO2_ppm)
        except:
            pass
        try:
            self.Carbon_Monoxide_CO_ppm = float(self.Carbon_Monoxide_CO_ppm)
        except:
            pass
        try:
            self.Temperature = float(self.Temperature)
        except:
            pass
        try:
            self.Pressure = float(self.Pressure)
        except:
            pass
        try:
            self.Humidity = float(self.Humidity)
        except:
            pass
        try:
            self.Noise = float(self.Noise)
        except:
            pass
        try:
            self.latitude = float(self.latitude)
        except:
            pass
        try:
            self.longitude = float(self.longitude)
        except:
            pass
        
        
    def insert(self):
        """Inserts a list of objects into the given connection
        Args:
            objs (list) - list of SQL helper objects
        """
        try:
             
            self.cursor.execute(self.get_insert_query(), self.get_values())
        except Exception as e:
            print(e)
            
        self.conn.commit()

    def get_values(self):
        """Get the values used for inseritng a SQL record
        Returns:
            tuple - tuple in ordered format for SQL table
        """
        values = (self.uRAD,self.location, self.Time_Str_Minute, self.Year,self.Month,
                  self.Day, self.Hour, self.Minute, self.Particulate_Matter_PM1, self.Particulate_Matter_PM25,
                  self.Particulate_Matter_PM10,
                  self.Ozone_O3_ppm, self.Nitrogen_Dioxide_NO2_ppm, self.Sulfer_Dioxide_SO2_ppm, 
                  self.Carbon_Monoxide_CO_ppm,self.VOC,self.Temperature,self.Pressure,self.Humidity,self.Noise,self.latitude,self.longitude)

        return values

    def get_insert_query(self):
        """Get the string SQL insert statement
        Returns:
            str - insert statement
        """
        _insert = f"""INSERT INTO 14000018_Minute_Average VALUES (%s,%s, %s, %s, %s,%s,%s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        return _insert

class Minute_1C_SQL_Writer_API_updating_one():
    def __init__(self,df, cursor, connection):
        self.cursor = cursor
        self.conn = connection

        """Load data from JSON object
        Args:
            user (dict) - json of object
        """
        
        self.uRAD = '1400001C'
        self.location = 'River Terrace'
        
        self.Time_Str_Minute = df.get('Time_Str',None)
        self.Year = int(df.get('Year', None))
        self.Month = int(df.get('Month', None))
        self.Day = int(df.get('Day', None))
        self.Hour = int(df.get('Hour',None))
        self.Minute = int(df.get('minute',None))
        
        self.Particulate_Matter_PM1 = df.get('pm1', None)
        self.Particulate_Matter_PM25 = df.get('pm25', None)
        self.Particulate_Matter_PM10 = df.get('pm10', None)
        self.Ozone_O3_ppm = df.get('gas1',None)
        self.Nitrogen_Dioxide_NO2_ppm = df.get('gas2',None)
        self.Sulfer_Dioxide_SO2_ppm = df.get('gas3', None)
        self.Carbon_Monoxide_CO_ppm = df.get('gas4', None)
        self.VOC = df.get('vocaqi',None)
        
        self.Temperature = df.get('temperature', None)
        self.Pressure = df.get('pressure', None)
        self.Humidity = df.get('humidity', None)
        self.Noise = df.get('noise',None)
        self.latitude = df.get('latitude', None)
        self.longitude = df.get('longitude',None)
        
        try:
            self.Particulate_Matter_PM1 = float(self.Particulate_Matter_PM1)
        except:
            pass
        try:
            self.VOC = float(self.VOC)
        except:
            pass
        try:
            self.Particulate_Matter_PM25 = float(self.Particulate_Matter_PM25)
        except:
            pass
        try:
            self.Particulate_Matter_PM10 = float(self.Particulate_Matter_PM10)
        except:
            pass
        try:
            self.Ozone_O3_ppm = float(self.Ozone_O3_ppm)
        except:
            pass
        try:
            self.Nitrogen_Dioxide_NO2_ppm = float(self.Nitrogen_Dioxide_NO2_ppm)
        except:
            pass
        try:
            self.Sulfer_Dioxide_SO2_ppm = float(self.Sulfer_Dioxide_SO2_ppm)
        except:
            pass
        try:
            self.Carbon_Monoxide_CO_ppm = float(self.Carbon_Monoxide_CO_ppm)
        except:
            pass
        try:
            self.Temperature = float(self.Temperature)
        except:
            pass
        try:
            self.Pressure = float(self.Pressure)
        except:
            pass
        try:
            self.Humidity = float(self.Humidity)
        except:
            pass
        try:
            self.Noise = float(self.Noise)
        except:
            pass
        try:
            self.latitude = float(self.latitude)
        except:
            pass
        try:
            self.longitude = float(self.longitude)
        except:
            pass
        
        
    def insert(self):
        """Inserts a list of objects into the given connection
        Args:
            objs (list) - list of SQL helper objects
        """
        try:
             
            self.cursor.execute(self.get_insert_query(), self.get_values())
        except Exception as e:
            print(e)
            
        self.conn.commit()

    def get_values(self):
        """Get the values used for inseritng a SQL record
        Returns:
            tuple - tuple in ordered format for SQL table
        """
        values = (self.uRAD,self.location, self.Time_Str_Minute, self.Year,self.Month,
                  self.Day, self.Hour, self.Minute, self.Particulate_Matter_PM1, self.Particulate_Matter_PM25,
                  self.Particulate_Matter_PM10,
                  self.Ozone_O3_ppm, self.Nitrogen_Dioxide_NO2_ppm, self.Sulfer_Dioxide_SO2_ppm, 
                  self.Carbon_Monoxide_CO_ppm,self.VOC,self.Temperature,self.Pressure,self.Humidity,self.Noise,self.latitude,self.longitude)

        return values

    def get_insert_query(self):
        """Get the string SQL insert statement
        Returns:
            str - insert statement
        """
        _insert = f"""INSERT INTO 1400001C_Minute_Average VALUES (%s, %s,%s, %s, %s,%s,%s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        return _insert


class Minute_58_SQL_Writer_API_updating_one():
    def __init__(self,df, cursor, connection):
        self.cursor = cursor
        self.conn = connection

        """Load data from JSON object
        Args:
            user (dict) - json of object
        """
        
        self.uRAD = '14000058'
        self.location = 'River Terrace'
        
        self.Time_Str_Minute = df.get('Time_Str',None)
        self.Year = int(df.get('Year', None))
        self.Month = int(df.get('Month', None))
        self.Day = int(df.get('Day', None))
        self.Hour = int(df.get('Hour',None))
        self.Minute = int(df.get('minute',None))
        
        self.Particulate_Matter_PM1 = df.get('pm1', None)
        self.Particulate_Matter_PM25 = df.get('pm25', None)
        self.Particulate_Matter_PM10 = df.get('pm10', None)
        self.Ozone_O3_ppm = df.get('gas1',None)
        self.Nitrogen_Dioxide_NO2_ppm = df.get('gas2',None)
        self.Sulfer_Dioxide_SO2_ppm = df.get('gas3', None)
        self.Carbon_Monoxide_CO_ppm = df.get('gas4', None)
        self.VOC = df.get('vocaqi',None)
        
        self.Temperature = df.get('temperature', None)
        self.Pressure = df.get('pressure', None)
        self.Humidity = df.get('humidity', None)
        self.Noise = df.get('noise',None)
        self.latitude = df.get('latitude', None)
        self.longitude = df.get('longitude',None)
        
        try:
            self.Particulate_Matter_PM1 = float(self.Particulate_Matter_PM1)
        except:
            pass
        
        try:
            self.VOC = float(self.VOC)
        except:
            pass
        
        try:
            self.Particulate_Matter_PM25 = float(self.Particulate_Matter_PM25)
        except:
            pass
        try:
            self.Particulate_Matter_PM10 = float(self.Particulate_Matter_PM10)
        except:
            pass
        try:
            self.Ozone_O3_ppm = float(self.Ozone_O3_ppm)
        except:
            pass
        try:
            self.Nitrogen_Dioxide_NO2_ppm = float(self.Nitrogen_Dioxide_NO2_ppm)
        except:
            pass
        try:
            self.Sulfer_Dioxide_SO2_ppm = float(self.Sulfer_Dioxide_SO2_ppm)
        except:
            pass
        try:
            self.Carbon_Monoxide_CO_ppm = float(self.Carbon_Monoxide_CO_ppm)
        except:
            pass
        try:
            self.Temperature = float(self.Temperature)
        except:
            pass
        try:
            self.Pressure = float(self.Pressure)
        except:
            pass
        try:
            self.Humidity = float(self.Humidity)
        except:
            pass
        try:
            self.Noise = float(self.Noise)
        except:
            pass
        try:
            self.latitude = float(self.latitude)
        except:
            pass
        try:
            self.longitude = float(self.longitude)
        except:
            pass
        
        
    def insert(self):
        """Inserts a list of objects into the given connection
        Args:
            objs (list) - list of SQL helper objects
        """
        try:
             
            self.cursor.execute(self.get_insert_query(), self.get_values())
        except Exception as e:
            print(e)
            
        self.conn.commit()

    def get_values(self):
        """Get the values used for inseritng a SQL record
        Returns:
            tuple - tuple in ordered format for SQL table
        """
        values = (self.uRAD,self.location, self.Time_Str_Minute, self.Year,self.Month,
                  self.Day, self.Hour, self.Minute, self.Particulate_Matter_PM1, self.Particulate_Matter_PM25,
                  self.Particulate_Matter_PM10,
                  self.Ozone_O3_ppm, self.Nitrogen_Dioxide_NO2_ppm, self.Sulfer_Dioxide_SO2_ppm, 
                  self.Carbon_Monoxide_CO_ppm,self.VOC,self.Temperature,self.Pressure,self.Humidity,self.Noise,self.latitude,self.longitude)

        return values

    def get_insert_query(self):
        """Get the string SQL insert statement
        Returns:
            str - insert statement
        """
        _insert = f"""INSERT INTO 14000058_Minute_Average VALUES (%s,%s, %s, %s, %s,%s,%s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        return _insert


    
class Minute_5A_SQL_Writer_API_updating_one():
    def __init__(self,df, cursor, connection):
        self.cursor = cursor
        self.conn = connection

        """Load data from JSON object
        Args:
            user (dict) - json of object
        """
        
        self.uRAD = '1400005A'
        self.location = 'River Terrace'
        
        self.Time_Str_Minute = df.get('Time_Str',None)
        self.Year = int(df.get('Year', None))
        self.Month = int(df.get('Month', None))
        self.Day = int(df.get('Day', None))
        self.Hour = int(df.get('Hour',None))
        self.Minute = int(df.get('minute',None))
        
        self.Particulate_Matter_PM1 = df.get('pm1', None)
        self.Particulate_Matter_PM25 = df.get('pm25', None)
        self.Particulate_Matter_PM10 = df.get('pm10', None)
        self.Ozone_O3_ppm = df.get('gas1',None)
        self.Nitrogen_Dioxide_NO2_ppm = df.get('gas2',None)
        self.Sulfer_Dioxide_SO2_ppm = df.get('gas3', None)
        self.Carbon_Monoxide_CO_ppm = df.get('gas4', None)
        self.VOC = df.get('vocaqi',None)
        
        self.Temperature = df.get('temperature', None)
        self.Pressure = df.get('pressure', None)
        self.Humidity = df.get('humidity', None)
        self.Noise = df.get('noise',None)
        self.latitude = df.get('latitude', None)
        self.longitude = df.get('longitude',None)
        
        try:
            self.Particulate_Matter_PM1 = float(Particulate_Matter_PM1)
        except:
            pass
        
        try:
            self.Particulate_Matter_PM25 = float(self.Particulate_Matter_PM25)
        except:
            pass
        try:
            self.Particulate_Matter_PM10 = float(self.Particulate_Matter_PM10)
        except:
            pass
        try:
            self.Ozone_O3_ppm = float(self.Ozone_O3_ppm)
        except:
            pass
        try:
            self.Nitrogen_Dioxide_NO2_ppm = float(self.Nitrogen_Dioxide_NO2_ppm)
        except:
            pass
        try:
            self.Sulfer_Dioxide_SO2_ppm = float(self.Sulfer_Dioxide_SO2_ppm)
        except:
            pass
        try:
            self.Carbon_Monoxide_CO_ppm = float(self.Carbon_Monoxide_CO_ppm)
        except:
            pass
        try:
            self.Temperature = float(self.Temperature)
        except:
            pass
        try:
            self.Pressure = float(self.Pressure)
        except:
            pass
        try:
            self.Humidity = float(self.Humidity)
        except:
            pass
        try:
            self.Noise = float(self.Noise)
        except:
            pass
        try:
            self.latitude = float(self.latitude)
        except:
            pass
        try:
            self.longitude = float(self.longitude)
        except:
            pass
        
        
    def insert(self):
        """Inserts a list of objects into the given connection
        Args:
            objs (list) - list of SQL helper objects
        """
        try:
             
            self.cursor.execute(self.get_insert_query(), self.get_values())
        except Exception as e:
            print(e)
            
        self.conn.commit()

    def get_values(self):
        """Get the values used for inseritng a SQL record
        Returns:
            tuple - tuple in ordered format for SQL table
        """
        values = (self.uRAD,self.location, self.Time_Str_Minute, self.Year,self.Month,
                  self.Day, self.Hour, self.Minute, self.Particulate_Matter_PM1, self.Particulate_Matter_PM25,
                  self.Particulate_Matter_PM10,
                  self.Ozone_O3_ppm, self.Nitrogen_Dioxide_NO2_ppm, self.Sulfer_Dioxide_SO2_ppm, 
                  self.Carbon_Monoxide_CO_ppm,self.VOC,self.Temperature,self.Pressure,self.Humidity,self.Noise,self.latitude,self.longitude)

        return values

    def get_insert_query(self):
        """Get the string SQL insert statement
        Returns:
            str - insert statement
        """
        _insert = f"""INSERT INTO 1400005A_Minute_Average VALUES (%s,%s, %s, %s, %s,%s,%s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        return _insert


def API_New_Data(API_string):
        API_header = {"X-User-id": '5517', "X-User-hash":"5c14f499c252f325c6dc43811bdce283"}

        
        r= requests.get(API_string, headers=API_header)
        r= r.json()
        new_API_data = r[-1]
        _time = new_API_data.get('time')
        time_list = Preprocessing_uRAD_API_min(_time)
        new_API_data.update({'Time_Str': time_list[0],'Year':time_list[1],'Month':time_list[2],'Day':time_list[3],'Hour':time_list[4],'minute':time_list[5]})
        return new_API_data
    
    
        
#### Step 3 Operation Part  ###################################################################################################################################################################################################


# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             
                             # host = 127.0.0.1 or host = 'localhost'(本地电脑)
                             port= 3306,
                             db = 'freshairdata',
                             user = 'freshairdc',
                             password = 'C8<CuFAFW7Vi<LUL',
                             cursorclass=pymysql.cursors.DictCursor)

#From our connection we need a cursor, which acts as our interface into the database
cur = connection.cursor()




cur = connection.cursor()
while 1 == 1:
    try:
        time.sleep(second)
        try:
            new_1A_data = API_New_Data('https://data.uradmonitor.com/api/v1/devices/1400001A/all/')
            Minute_1A_SQL_Writer_API_updating_one(new_1A_data,cur,connection).insert()
        except:
            pass

        try:
            new_1C_data = API_New_Data('https://data.uradmonitor.com/api/v1/devices/1400001C/all/')
            Minute_1C_SQL_Writer_API_updating_one(new_1C_data,cur,connection).insert()
        except:
            pass

        try:
            new_18_data = API_New_Data('https://data.uradmonitor.com/api/v1/devices/14000018/all/')
            Minute_18_SQL_Writer_API_updating_one(new_18_data,cur,connection).insert()
        except:
            pass

        try:
            new_58_data = API_New_Data('https://data.uradmonitor.com/api/v1/devices/14000058/all/')
            Minute_58_SQL_Writer_API_updating_one(new_58_data,cur,connection).insert()
        except:
            pass

        try:
            new_5A_data = API_New_Data('https://data.uradmonitor.com/api/v1/devices/1400005A/all/')
            Minute_5A_SQL_Writer_API_updating_one(new_5A_data,cur,connection).insert()
        except:
            pass       
    except:
        pass
