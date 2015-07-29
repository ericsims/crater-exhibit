# Limit Switch

import yaml

class LimitSwitch:
  settings = 0
  pin = None
  def __init__(self, pin):
    f = open('settings.yaml')
    self.settings = yaml.safe_load(f)
    f.close()
    self.pin = pin
    
  def setPin(self, pin):
    self.pin = pin
    
  def printPin(self):
    print "Current Limit Switch Pin: "
    print self.pin
  
  def getPin(self):
    return self.pin