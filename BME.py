import board
import digitalio
import busio
import time
import adafruit_bme280

# OR create library object using our Bus SPI port
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
bme_cs = digitalio.DigitalInOut(board.D5)
bme280 = None

def init():
	global bme280
	try:
	    bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, bme_cs)
	    return 0
	except:
            print("PTH Initialization Error")
            return -1

def temp():
	try:
	    return bme280.temperature
	except:
            print("PTH Temp Error")
            return -1

def humidity():
	try:
	    return bme280.humidity
	except:
            print("PTH Hum Error")
            return -1

def pressure():
	try:
	    return bme280.pressure
	except:
            print("PTH Pres Error")
            return -1


def data():
	try:
	    return [temp(),humidity(),pressure()]
	except:
            return [-1,-1,-1]
