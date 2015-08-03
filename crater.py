# Crater Maker Exhibit

from Axis import Axis
from Limit_Switch import LimitSwitch
from Relay import Relay
from Motor import Motor
import time
import platform
import yaml

if(platform.system() == "Linux"):
  ON_PI = 1
  from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
  import RPi.GPIO as GPIO
  GPIO.setwarnings(False)  
  GPIO.setmode(GPIO.BOARD)
else:
  print "\nWARNING: Not on Linux!\n"
  ON_PI = 0

  
f = open('settings.yaml')
settings = yaml.safe_load(f)
f.close()

mh0 = None
mh1 = None

if(ON_PI):
  mh0 = Adafruit_MotorHAT(0x60)
  mh1 = Adafruit_MotorHAT(0x61)
  
  
sol0 = Relay(18, True)
sol1 = Relay(22, True)
sol2 = Relay(7, True) 
sol0.setState(1)
sol1.setState(1)
sol2.setState(1)

x = Axis()
x.attach(Motor(mh0, 0), LimitSwitch(0))
x.printMotorAttachments()
x.homeAxis()

time.sleep(2)
