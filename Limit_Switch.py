# Limit Switch

import platform

# Are we on the raspberry pi?
if(platform.system() == "Linux"):
  import RPi.GPIO as GPIO
  ON_PI = 1
else:
  ON_PI = 0
  
class LimitSwitch:
  settings = 0
  pin = None
  def __init__(self, pin):
    self.setPinNumber(pin)
    
  # Change pin number
  def setPinNumber(self, pin):
    self.pin = pin
    if(ON_PI):
      # Configure input pin
      GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
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
      
  # Set a callback function for the FALLING edge of a switch
  def setCallback(self, call):
    if(ON_PI):
      GPIO.add_event_detect(self.pin, GPIO.FALLING, callback = call)
