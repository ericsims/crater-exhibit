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
      GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
  def setPinNumber(self, pin):
    self.pin = pin
    
  def printPin(self):
    print "Current Limit Switch Pin: "
    print self.getPin()
  
  def getPinNumber(self):
    return self.pin
    
  def getState(self):
    if(ON_PI):
      return GPIO.input(self.pin)
    else:
      return None 

  def setCallback(self, call):
    if(ON_PI):
      GPIO.add_event_detect(self.pin, GPIO.FALLING, callback = call)
