import BME
import LUX
import config
from Adafruit_IO import Client, Feed
import time



BME.init()
LUX.init()

vars = config.get()

ADAFRUIT_IO_KEY = vars['ADAFRUIT_IO_KEY']

ADAFRUIT_IO_USERNAME = vars['ADAFRUIT_IO_USERNAME']

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

temperature_feed = aio.feeds('temperature')
humidity_feed = aio.feeds('humidity')
pressure_feed = aio.feeds('pressure')
light_feed = aio.feeds('light')

count = 0
maxcount = 10

while True:
    temp, humidity, pressure = BME.data()
    light = LUX.lux()
    print('Temp={0:0.1f}*C Humidity={1:0.1f}% Pressure={2:0.1f} Light={3:0.1f}'.format(temp, humidity, pressure, light))
    # Send humidity and temperature feeds to Adafruit IO
    temperature = '%.2f'%(temp)
    humidity = '%.2f'%(humidity)
    pressure = '%.2f'%(pressure)
    light = '%.2f'%(light)
    if (count == maxcount):
        aio.send(temperature_feed.key, str(temperature))
        aio.send(humidity_feed.key, str(humidity))
        aio.send(pressure_feed.key, str(pressure))
        aio.send(light_feed.key, str(light))
        count = 0
    count += 1
    time.sleep(1)
