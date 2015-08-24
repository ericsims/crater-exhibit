# Dropper Class

import time

class Dropper:
  def __init__(self, solenoid, photocell):
    self.solenoid = solenoid
    self.photocell = photocell

  def drop(self, force = False):
    # Check repeatedly for ball for 1 second
    for i in range(10):
      time.sleep(0.1)
      if(self.isFull() or force):
        # Wait, drop, wait, close, wait
        time.sleep(0.25)
        self.solenoid.setState(1)
        time.sleep(0.25)
        self.solenoid.setState(0)
        time.sleep(0.25)
        return
    print "No Ball Present"
#  feeder.index()
  
  def isFull(self):
    return not self.photocell.getState()