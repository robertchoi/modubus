import threading, time, subprocess, logging, minimalmodbus
from time import sleep

meter0 = minimalmodbus.Instrument("/dev/ttyUSB0", 1)    # Volt
meter1 = minimalmodbus.Instrument("/dev/ttyUSB1", 1)    # Ampere

meter0.serial.baudrate = 9600
meter1.serial.baudrate = 9600

meter0.mode = minimalmodbus.MODE_RTU
meter1.mode = minimalmodbus.MODE_RTU

logging.basicConfig()


def read_meter():

    filename = 'v2g-'+time.strftime('%Y%m%d')+'.csv'
#    print (filename)

    Dir_FlagStr = 'FWD ,'       # 'REV"
    meter0_value = meter0.read_register(0, 1)
    meter1_value = meter1.read_register(0, 1)

    print(time.strftime('%Y-%m-%d %X ')+Dir_FlagStr)
    print(meter0_value, 'V,  ', meter1_value, 'A')

    if (meter0_value > 9.9):
        print('DB write......')
        file = open(filename, 'a+')
        file.write(time.strftime('%Y-%m-%d , %X ,')+Dir_FlagStr+' -  ,')
        file.write('{} , {}\n'.format(meter0_value,meter1_value))
        file.close()

def main():
    while True:
        read_meter()
        sleep(3)

if __name__ == "__main__":
  main()
