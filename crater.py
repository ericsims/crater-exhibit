# Crater Maker Exhibit

from Axis import Axis
from Limit_Switch import LimitSwitch
from Relay import Relay
from Motor import Motor
from Feeder import Feeder
from Dropper import Dropper
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

  
print "Loading settings and initializing"
  
f = open('settings.yaml')
settings = yaml.safe_load(f)
f.close()

mh = [0, 0]

if(ON_PI):
  mh = [ Adafruit_MotorHAT(settings['StepperHat']['addr'][0]), Adafruit_MotorHAT(settings['StepperHat']['addr'][1]) ]

  
feeder = Feeder(Motor(mh[settings['Feeder']['mh']], settings['Feeder']['index']))
dropper = Dropper(Relay(settings['Dropper']['solenoid']), LimitSwitch(settings['Dropper']['photoPin']))

x = Axis()
xSettings = settings['Axis']['X']
for i in range(len(xSettings)):
  x.attach(Motor(mh[xSettings[i]['mh']], xSettings[i]['index'], xSettings[i]['invert']), LimitSwitch(xSettings[i]['homeLimitSwitch']), LimitSwitch(xSettings[i]['endLimitSwitch']))

y = Axis()
ySettings = settings['Axis']['Y']
for i in range(len(ySettings)):
  y.attach(Motor(mh[ySettings[i]['mh']], ySettings[i]['index'], ySettings[i]['invert']), LimitSwitch(ySettings[i]['homeLimitSwitch']), LimitSwitch(ySettings[i]['endLimitSwitch']))

print "Ready!"  

print "Homing X and Y Axes"
#x.homeAxis()
#y.homeAxis()

#while(not x.atHome() or not y.atHome()) and ON_PI:
#  time.sleep(0.5)
  
print "X and Y Axes Homed"

while(True):
  while(dropper.isFull()):
    time.sleep(0.1)
  time.sleep(0.5)
  dropper.drop()
#  feeder.index()
  time.sleep(0.2)
raw_input("Press Enter to continue...")

x.stop()
y.stop()
