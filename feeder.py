from Adafruit_MotorHAT import Adafruit_MotorHAT
from Motor import Motor
import time
mh1 = Adafruit_MotorHAT(0x61)
rotator = Motor(mh1, 1)
for i in range(8):
  rotator.degrees(51)
  time.sleep(0.5)
raw_input("Press enter to end program...")
rotator.stop()
