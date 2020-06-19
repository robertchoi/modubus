import minimalmodbus
import serial

instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)

instrument.serial.baudrate = 9600

temperature = instrument.read_register(6, 1)
print(temperature)

temperature = instrument.read_register(0, 1)
print(temperature)