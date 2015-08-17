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
#xSettings = settings['Axis']['X']
#for i in range(len(xSettings)):
#  x.attach(Motor(mh[xSettings[i]['mh']], xSettings[i]['index'], xSettings[i]['invert']), LimitSwitch(xSettings[i]['homeLimitSwitch']), LimitSwitch(xSettings[i]['endLimitSwitch']))

y = Axis()
#ySettings = settings['Axis']['Y']
#for i in range(len(ySettings)):
#  y.attach(Motor(mh[ySettings[i]['mh']], ySettings[i]['index'], ySettings[i]['invert']), LimitSwitch(ySettings[i]['homeLimitSwitch']), LimitSwitch(ySettings[i]['endLimitSwitch']))

y.attach(Motor(mh[1], 1, 1), LimitSwitch(35), LimitSwitch(37))

print "Ready!"  

print "Homing X and Y Axes"
#x.homeAxis()
y.homeAxis()

while(not y.atHome()) and ON_PI:
  time.sleep(0.5)
  
print "X and Y Axes Homed"

done = False
while(not done):
  txt = raw_input("Press Enter to continue...")
  if(txt == "r"):
    y.move(0)
  if(txt == "l"):
    y.move(1)
  if(txt == "s"):
    y.stop()
  if(txt == "q"):
    done = True
  if(txt == "drop"):
    dropper.drop()
  if(txt == "drop -f"):
    dropper.drop(True)

x.stop()
y.stop()
