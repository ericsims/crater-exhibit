# Axis Object Declaration
#from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
from Limit_Switch import LimitSwitch
import yaml
import platform
import atexit
import threading
import random
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
    
  def attach(self, addr, index, LimitSwitch, direction = 0):
    self.motors.append({'addr': addr, 'index': index, 'limitSwitch': LimitSwitch, 'direction': direction})
    
  def printMotorAttachments(self):
    print "Current Motors Attached: "
    print self.motors
    
  def homeAxis(self):
    print self.motors[0]["limitSwitch"].getState()