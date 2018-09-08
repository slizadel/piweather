import bme280
import smbus2
from time import sleep


port = 1
address = 0x77
bus = smbus2.SMBus(port)

while True:
    bme280_data = bme280.sample(bus, address)
    humidity = bme280_data.humidity
    pressure = bme280_data.pressure
    ambeint_temperature = bme280_data.temperature
    print(humidity, pressure, ambeint_temperature)
    sleep(1)
