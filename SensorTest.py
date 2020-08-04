import BME
import LUX
import config
#from Adafruit_IO import Client, Feed
import time
import os
import sys
import threading

BME.init()
LUX.init()

vars = config.get()

deployment = vars['DEPLOYMENT']
relay = vars['ID']

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
    print('Temp={0:0.1f}*C Humidity={1:0.1f}% Pressure={2:0.1f} Light={3:0.1f}'.format(temp, humidity, pressure, light))
    #temperature = '%.2f'%(temp)
    #humidity = '%.2f'%(humidity)
    #pressure = '%.2f'%(pressure)
    #light = '%.2f'%(light)
    time.sleep(1)
