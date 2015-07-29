# Limit Switch

import platform
import yaml
if(platform.system() == "Linux"):
  import RPi.GPIO as GPIO
  ON_PI = 1
else:
  ON_PI = 0
  
class LimitSwitch:
  settings = 0
  pin = None
  def __init__(self, pin):
    f = open('settings.yaml')
    self.settings = yaml.safe_load(f)
    f.close()
    self.pin = pin
    if(ON_PI):
      GPIO.setup(self.pin, GPIO.IN)
    
  def setPin(self, pin):
    self.pin = pin
    
  def printPin(self):
    print "Current Limit Switch Pin: "
    print self.getPin()
  
  def getPin(self):
    return self.pin
    
  def getState(self):
    if(ON_PI):
      return GPIO.input(self.pin)
    else:
      return None
  