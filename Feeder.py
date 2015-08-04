from Adafruit_MotorHAT import Adafruit_MotorHAT
from Motor import Motor
import time

class Feeder:
  def __init__(self, motor):
    self.rotator = motor
    for i in range(8):
      rotator.degrees(51)
      time.sleep(0.5)
    raw_input("Press enter to end program...")
    rotator.stop()

  def index(self, direction = 0):
    self.rotator.degrees(51, direction)
    
  def stop(self)
    self.rotator.stop()
    
  def release(self)
    self.rotator.release()