# Dropper Class

import time

class Dropper:
  def __init__(self, solenoid, photocell):
    self.solenoid = solenoid
    self.photocell = photocell

  def drop(self, wait = True):
  for i in range(50):
    time.sleep(0.1)
    if((dropper.isFull()):
      time.sleep(0.5)
      self.solenoid.setState(1)
      time.sleep(0.5)
      self.solenoid.setState(0)
      time.sleep(0.5)
      return
  print "No Ball Present"
#  feeder.index()
  time.sleep(0.2)
    
  def isFull(self):
    return self.photocell.getState()
