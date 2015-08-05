# Feeder Class

class Feeder:
  def __init__(self, motor):
    self.rotator = motor

  def index(self, direction = 0):
    self.rotator.degrees(51, direction)
    
  def stop(self):
    self.rotator.stop()
    
  def release(self):
    self.rotator.release()