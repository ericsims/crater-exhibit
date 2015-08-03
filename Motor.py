# Motor Object

#!/usr/bin/python
import time
import atexit
import threading
import random
import platform
import yaml

if(platform.system() == "Linux"):
  ON_PI = 1
  from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
  stepstyles = [Adafruit_MotorHAT.SINGLE, Adafruit_MotorHAT.DOUBLE, Adafruit_MotorHAT.INTERLEAVE, Adafruit_MotorHAT.MICROSTEP]
else:
  ON_PI = 0

f = open('settings.yaml')
settings = yaml.safe_load(f)
f.close()


class Motor:

  if(ON_PI):

    def __init__(self, motorHat, index):
      self.motorHat = motorHat
      self.st1 = threading.Thread()
      self.motorIndex = index
      self.stepper = mh.getStepper(200, 1)  	# 200 steps/rev, motor port #1
      self.st1 = threading.Thread(target=stepper_worker, args=(self.stepper, randomsteps, dir, stepstyles[0],))
      self.st1.start()

      
    def stopMotor(self):
      self.st1.stop()

    # recommended for auto-disabling motors on shutdown!
    def turnOffMotors(self):
      mh.getMotor(self.motorIndex * 2 - 1).run(Adafruit_MotorHAT.RELEASE)
      mh.getMotor(self.motorIndex * 2).run(Adafruit_MotorHAT.RELEASE)

    atexit.register(turnOffMotor)

    myStepper1.setSpeed(60)  		# 30 RPM

    def stepper_worker(stepper, numsteps, direction, style):
      #print("Steppin!")
      stepper.step(numsteps, direction, style)
      #print("Done")

  while (True):
    if not st1.isAlive():
      randomdir = random.randint(0, 1)
      print("Stepper 1"),
      if (randomdir == 0):
        dir = Adafruit_MotorHAT.FORWARD
        print("forward"),
      else:
        dir = Adafruit_MotorHAT.BACKWARD
        print("backward"),
      randomsteps = random.randint(10,50)
      print("%d steps" % randomsteps)
      st1 = threading.Thread(target=stepper_worker, args=(myStepper1, randomsteps, dir, stepstyles[random.randint(0,3)],))
      st1.start()

    if not st2.isAlive():
      print("Stepper 2"),
      randomdir = random.randint(0, 1)
      if (randomdir == 0):
        dir = Adafruit_MotorHAT.FORWARD
        print("forward"),
      else:
        dir = Adafruit_MotorHAT.BACKWARD
        print("backward"),

      randomsteps = random.randint(10,50)		
      print("%d steps" % randomsteps)

      st2 = threading.Thread(target=stepper_worker, args=(myStepper2, randomsteps, dir, stepstyles[random.randint(0,3)],))
      st2.start()