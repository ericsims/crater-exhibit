# Crater Maker Exhibit

from Axis import Axis
from Limit_Switch import LimitSwitch
from Relay import Relay
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

if(ON_PI):
  mh0 = Adafruit_MotorHAT(0x60)
  mh1 = Adafruit_MotorHAT(0x61)
  
  
sol0 = Relay(18, True)
sol1 = Relay(22, True)
sol2 = Relay(7, True)
sol2.setState(0)


x = Axis()
x.attach(settings['StepperHat']['addr'][0], 0, LimitSwitch(0), 0)
x.printMotorAttachments()
x.homeAxis()
