from Adafruit_MotorHAT import Adafruit_MotorHAT
from Motor import Motor
mh1 = Adafruit_MotorHAT(0x61)
rotator = Motor(mh1, 1)
rotator.run()
raw_input("Press enter to end program...")
rotator.stop()
