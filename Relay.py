# Relay

import platform
import atexit

# Are we on the raspberry pi?
if(platform.system() == "Linux"):
  import RPi.GPIO as GPIO
  ON_PI = 1
else:
  ON_PI = 0
  
class Relay:
  settings = 0
  pin = None
  def __init__(self, pin, invert = 0):
    self.setPinNumber(pin)
    self.invert = not invert
    atexit.register(self.exit)
    
  def exit(self):
    self.setState(0)
  
  # Change pin number
  def setPinNumber(self, pin):
    self.pin = pin
    if(ON_PI):
      # Configure the output pin
      GPIO.setup(self.pin, GPIO.OUT)
      self.setState(0);
    
  def printPin(self):
    print "Current Relay Pin: "
    print self.getPin()
  
  def getPinNumber(self):
    return self.pin
    
  def getState(self):
    return currentState
  
  # Set the output state
  def setState(self, state):
    if(ON_PI):
      if(self.invert):
        GPIO.output(self.pin, 1 - state)
      else:
        GPIO.output(self.pin, state)
      self.currentState = state
