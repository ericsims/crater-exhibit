# Relay

import platform
import yaml
if(platform.system() == "Linux"):
  import RPi.GPIO as GPIO
  ON_PI = 1
else:
  ON_PI = 0
  
class Relay:
  settings = 0
  pin = None
  def __init__(self, pin):
    f = open('settings.yaml')
    self.settings = yaml.safe_load(f)
    f.close()
    self.pin = pin
    if(ON_PI):
      GPIO.setup(self.pin, GPIO.OUT)
      setState(0);
    
  def setPinNumber(self, pin):
    self.pin = pin
    
  def printPin(self):
    print "Current Relay Pin: "
    print self.getPin()
  
  def getPinNumber(self):
    return self.pin
    
  def getState(self):
    return currentState
  
  def setState(self, state):
    if(ON_PI):
      GPIO.output(self.pin, state)
      self.currentState = state