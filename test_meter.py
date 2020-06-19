import threading, time, subprocess, logging, minimalmodbus
from apscheduler.scheduler import Scheduler
from time import sleep

meter0 = minimalmodbus.Instrument("/dev/ttyUSB0", 1)
meter1 = minimalmodbus.Instrument("/dev/ttyUSB1", 1)

meter0.serial.baudrate = 9600
meter1.serial.baudrate = 9600

meter0.mode = minimalmodbus.MODE_RTU
meter1.mode = minimalmodbus.MODE_RTU

logging.basicConfig()

sched = Scheduler()
sched.start()

def read_meter():

    meter0_value = meter0.read_register(0, 1)
    meter1_value = meter1.read_register(0, 1)

    print(time.strftime('%Y%m%d %X '))
    print(meter0_value, meter1_value)
    file = open('meter_data.txt', 'w+')
    file.write(time.strftime('%Y%m%d %X '))
    file.write('{} {}\n'.format(meter0_value,meter0_value))
    file.close()

  
def main():
    sched.add_cron_job(read_meter, second='*/5')

    while True:
        sleep(1)

if __name__ == "__main__":
  main()
