import minimalmodbus

instrument = minimalmodbus.Instrument('/dev/ttyUSB1', 1)

instrument.serial.baudrate = 9600

temperature = instrument.read_register(6, 2)
print(temperature)

temperature = instrument.read_register(0, 2)
print(temperature)