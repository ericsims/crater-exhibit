# Crater Maker Exhibit

#!/usr/bin/python
from Axis import Axis
from Limit_Switch import LimitSwitch
from Relay import Relay
from Motor import Motor
from Feeder import Feeder
from Dropper import Dropper
import time
import platform

# Limit Switch Pin Declarations

LS = [11, 12, 13, 15, 35, 37, 38]

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
  
mh = [0, 0]

if(ON_PI):
  mh = [ Adafruit_MotorHAT(0x60), Adafruit_MotorHAT(0x61) ]

  
feeder = Feeder(Motor(mh[1], 2))
dropper = Dropper(Relay(18, 1), LimitSwitch(16)) # Note, pin 16 is the Photocell, not a physical limit switch

x = Axis()
x.attach(Motor(mh[0], 1, 1), LimitSwitch(LS[2]), LimitSwitch(LS[3]))
x.attach(Motor(mh[0], 2, 1), LimitSwitch(LS[1]), LimitSwitch(LS[4]))

y = Axis()
y.attach(Motor(mh[1], 1, 1), LimitSwitch(LS[6]), LimitSwitch(LS[5]))

print "Ready!"  

print "Homing X and Y Axes"
#x.homeAxis()
y.homeAxis()


# wait for x and y axis to home
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
