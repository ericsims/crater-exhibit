# Dropper Class

import time

class Dropper:
  def __init__(self, solenoid, photocell):
    self.solenoid = solenoid
    self.photocell = photocell

  def drop(self):
    self.solenoid.setState(1)
    time.sleep(1)
    self.solenoid.setState(0)
    time.sleep(0.5)
    
  def isFull(self):
    return self.photocell.getState()