import minimalmodbus
import serial

instrument = minimalmodbus.Instrument('/dev/ttyUSB1', 1)

instrument.serial.baudrate = 9600
instrument.mode = minimalmodbus.MODE_RTU

temperature = instrument.read_register(6, 1)
print(temperature)

temperature = instrument.read_register(0, 1)
print(temperature)