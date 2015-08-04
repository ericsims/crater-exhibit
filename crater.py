# Crater Maker Exhibit

from Axis import Axis
from Limit_Switch import LimitSwitch
from Relay import Relay
from Motor import Motor
from Feeder import Feeder
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

mh0 = None
mh1 = None

if(ON_PI):
  mh = [ Adafruit_MotorHAT(settings['StepperHat'][0]), Adafruit_MotorHAT(settings['StepperHat'][1]) ]
else:
  mh = [0,0]
  
solenoids = settings['Solenoid']
sol0 = Relay(solenoids[0]['addr'], solenoids[0]['invert'])
sol1 = Relay(solenoids[1]['addr'], solenoids[1]['invert'])
sol2 = Relay(solenoids[2]['addr'], solenoids[1]['invert'])

feeder = Feeder(Motor(mh[settings['Feeder']['mh']], settings['Feeder']['index']))

x = Axis()
xSettings = settings['Axis']['X']
for i in range(len(xSettings)):
  x.attach(Motor(xSettings[i]['mh'], xSettings[i]['index'], xSettings[i]['invert']), LimitSwitch(xSettings[i]['homeLimitSwitch']), LimitSwitch(xSettings[i]['endLimitSwitch']))

y = Axis()
ySettings = settings['Axis']['Y']
for i in range(len(ySettings)):
  y.attach(Motor(ySettings[i]['mh'], ySettings[i]['index'], ySettings[i]['invert']), LimitSwitch(ySettings[i]['homeLimitSwitch']), LimitSwitch(ySettings[i]['endLimitSwitch']))

print "Ready!"  

print "Homing X and Y Axes"
x.homeAxis()
y.homeAxis()

while(not x.atHome() or not y.atHome()) and ON_PI:
  time.sleep(0.5)

for i in range(8):
  feeder.index()
  time.sleep(0.5)

raw_input("Press Enter to continue...")

x.stop()
