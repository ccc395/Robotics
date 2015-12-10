#!/usr/bin/python
# MOTORS
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.ADC as ADC
import time

#right
PWM.start("P9_14", 0, 1000, 0)
#left
PWM.start("P9_16", 0, 1000, 0)

#Right motor
GPIO.setup("P9_11", GPIO.OUT); GPIO.output("P9_11", GPIO.LOW)
GPIO.setup("P9_12", GPIO.OUT); GPIO.output("P9_12", GPIO.LOW)
#left motor
GPIO.setup("P9_13", GPIO.OUT); GPIO.output("P9_13", GPIO.LOW)
GPIO.setup("P9_15", GPIO.OUT); GPIO.output("P9_15", GPIO.LOW)

#Forward
PWM.set_duty_cycle("P9_16", 50)
PWM.set_duty_cycle("P9_14", 50)
raw_input('Press enter to activate')
GPIO.output("P9_13", GPIO.HIGH)
GPIO.output("P9_15", GPIO.LOW)
GPIO.output("P9_11", GPIO.HIGH)
GPIO.output("P9_12", GPIO.LOW)
raw_input('Press enter to stop')
PWM.stop("P9_16")
PWM.stop("P9_14")


GPIO.cleanup()
PWM.cleanup()

#Setup the ADC
ADC.setup()
print "Test IR Sensor"
i=0
while i <= 0:
  print("Dist",  ADC.read_raw("P9_39"))
  print("x",  ADC.read_raw("P9_37"))
  print("y",  ADC.read_raw("P9_38"))
  time.sleep(0.25)

