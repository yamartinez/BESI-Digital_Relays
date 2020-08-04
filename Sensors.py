import BME
import LUX
import config
#from Adafruit_IO import Client, Feed
import time
import os
import sys
import threading
from Heartbeats import *

BME.init()
LUX.init()

vars = config.get()

deployment = vars['DEPLOYMENT']
relay = vars['ID']
lightpath = vars['LUX_PATH']
temppath = vars['TEMPERATURE_PATH']
prespath = vars['PRESSURE_PATH']
humpath = vars['HUMIDITY_PATH']

print(deployment)
print(relay)
print(lightpath)
print(temppath)
print(prespath)
print(humpath)

#ADAFRUIT_IO_KEY = vars['ADAFRUIT_IO_KEY']

#ADAFRUIT_IO_USERNAME = vars['ADAFRUIT_IO_USERNAME']

#aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

#temperature_feed = aio.feeds('temperature')
#humidity_feed = aio.feeds('humidity')
#pressure_feed = aio.feeds('pressure')
#light_feed = aio.feeds('light')

#count = 0
#maxcount = 10

def CollectSound():
    import Sound
    while(1):
        Sound.GetData()

SoundThread = threading.Thread(target=CollectSound, args=(), daemon=True)
SoundThread.start()

while True:
    temp, humidity, pressure = BME.data()
    light = LUX.lux()
    #print('Temp={0:0.1f}*C Humidity={1:0.1f}% Pressure={2:0.1f} Light={3:0.1f}'.format(temp, humidity, pressure, light))
    temperature = '%.2f'%(temp)
    humidity = '%.2f'%(humidity)
    pressure = '%.2f'%(pressure)
    light = '%.2f'%(light)
#    if (count == maxcount):
#        aio.send(temperature_feed.key, str(temperature))
#        aio.send(humidity_feed.key, str(humidity))
#        aio.send(pressure_feed.key, str(pressure))
#        aio.send(light_feed.key, str(light))
#        count = 0
#    count += 1
    sendHeartBeat(relay,deployment,light,temperature,pressure,humidity)

    try:
        with open(lightpath,'a+') as file:
            file.write(time.ctime()+","+light+"\n")
    except Exception as e:
        print(e)
    try:
        with open(temppath,'a+') as file:
            file.write(time.ctime()+","+temperature+"\n")
    except Exception as e:
        print(e)
    try:
        with open(prespath,'a+') as file:
            file.write(time.ctime()+","+pressure+"\n")
    except Exception as e:
        print(e)
    try:
        with open(humpath,'a+') as file:
            file.write(time.ctime()+","+humidity+"\n")
    except Exception as e:
        print(e)

    time.sleep(1)
