# Axis Object Declaration
from Limit_Switch import LimitSwitch
import yaml
import platform
import atexit
import threading
import random
import time
if(platform.system() == "Linux"):
  import RPi.GPIO as GPIO
  from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
  ON_PI = 1
else:
  ON_PI = 0


class Axis:
  settings = 0
  motors = []
  def __init__(self):
    f = open('settings.yaml')
    self.settings = yaml.safe_load(f)
    f.close()
    
  def attach(self, motor, LimitSwitchHome):
    self.motors.append({'motor': motor, 'limitSwitchHome': LimitSwitchHome, 'limitSwitchEnd': LimitSwitchEnd})
    self.motors[-1]['limitSwitchHome'].setCallback(self.motors[-1]['motor'].stop)
    self.motors[-1]['limitSwitchEnd'].setCallback(self.motors[-1]['motor'].stop)
    
  def printMotorAttachments(self):
    print "Current Motors Attached: "
    print self.motors
    
  def homeAxis(self):
    self.motors[0]['motor'].run()

  def move(self,direction = 0):
    for i in range(len(self.motors)):
      if(direction && self.motors[i]['limitSwitchHome'].getState()):
        self.motors[i]['motor'].run(0)
      else if(self.motors[i]['limitSwitchEnd'].getState()):
        self.motors[i]['motor'].run(1)

  def stop(self):
    for i in range(len(self.motors)):
      self.motors[i]['motor'].stop()
