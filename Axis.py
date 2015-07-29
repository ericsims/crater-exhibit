# Axis Object Declaration
#from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
from Limit_Switch import LimitSwitch
import yaml

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