import threading, time, subprocess, logging, minimalmodbus
from apscheduler.scheduler import Scheduler
from time import sleep
wattson = minimalmodbus.Instrument("/dev/ttyUSB0", 1)
wattson.serial.baudrate = 9600
logging.basicConfig()

sched = Scheduler()
sched.start()

def read_meter():

  TEC  = round(wattson.read_float(768), 3) # total energy consumed KWh
  CONS = int(wattson.read_float(770)*1000) # total real power Watts
  VOLT = round(wattson.read_float(792), 1) # voltage
  LEG1 = int(wattson.read_float(806)*1000) # watts A
  LEG2 = int(wattson.read_float(808)*1000) # watts B
  GENW = int(wattson.read_float(810)*1000) # watts C (PV output)
  IMPA = round(wattson.read_float(832), 3) # import A KWh
  IMPB = round(wattson.read_float(834), 3) # import B KWh
  EXPA = round(wattson.read_float(840), 3) # export A KWh
  EXPB = round(wattson.read_float(842), 3) # export B KWh
  NETA = round(wattson.read_float(848), 3) # net A KWh
  NETB = round(wattson.read_float(850), 3) # net B KWh
  NETC = round(wattson.read_float(852), 3) # net C KWh
  HTOT = LEG1 + LEG2

  if GENW < 50: # if PV output < 50 Watts set it to zero Watts
     GENW = 0

  file = open('/tmp/meter_data.txt', 'w+')
  file.write(time.strftime('%Y%m%d %X '))
  file.write('{} {} {} {} {} {} {} {} {} {} {} {}\n'.format(GENW,HTOT,VOLT,CONS,TEC,IMPA,IMPB,EXPA,EXPB,NETA,NETB,NETC))
  file.close()

  subprocess.call('/opt/send-to-eorg.sh') # call the bash file to transmit the data

###
I chose to reset the meter every day at midnight to avoid
the need to calculate each day's energy comsumption.
That way, the readings at the end of each day ARE the day's
energy consumption and PV production.
###
def reset_meter():
  sleep(2)
  wattson.write_register(135, 0xA5A5, 0, 6)  # reset
  wattson.write_register(135, 0x5A5A, 0, 6)
  sleep(2)
  wattson.write_register(135, 0xA5A5, 0, 6)  # reset
  wattson.write_register(135, 0x5A5A, 0, 6)
  
###
Advanced Python Scheduler uses a syntax very similar to
the CRON utility. Unlike CRON, APS has one second resolution.
IOW, jobs can be scheduled as often as once per second.
###
def main():
  sched.add_cron_job(read_meter, second='*/5')
  sched.add_cron_job(reset_meter, hour='23', minute='59', second='52')

  while True:
    sleep(1)

if __name__ == "__main__":
  main()
