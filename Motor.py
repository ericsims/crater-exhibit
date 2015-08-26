# Motor Object

import time
import atexit
import threading
import random
import platform

# Are we on the raspberry pi?
if(platform.system() == "Linux"):
  ON_PI = 1
  from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
  stepstyles = [Adafruit_MotorHAT.SINGLE, Adafruit_MotorHAT.DOUBLE, Adafruit_MotorHAT.INTERLEAVE, Adafruit_MotorHAT.MICROSTEP]
else:
  ON_PI = 0

class Motor:

  def __init__(self, motorHat, index, invert = False):
    self.mh = motorHat
    self.st1 = threading.Thread()
    self.motorIndex = index
    self.invert = invert
    self.done = False
    if(ON_PI):
      # Declare stepper motor and set speed
      self.stepper = self.mh.getStepper(200, index)  	# 200 steps/rev, motor port #1
      self.stepper.setSpeed(10000)
    atexit.register(self.release)
    # self.test()
   
  # Stop the motor
  def stop(self):
    self.done = True

  # Release motor control
  def release(self):
    self.stop()
    time.sleep(0.010)
    if(ON_PI):
      self.mh.getMotor(self.motorIndex * 2 - 1).run(Adafruit_MotorHAT.RELEASE)
      self.mh.getMotor(self.motorIndex * 2).run(Adafruit_MotorHAT.RELEASE)

  # Step the motor
  def step(self, direction = 0, steps = 1, style = None):
    if(ON_PI):
      if(style == None):
        # default to double stepping
        style = Adafruit_MotorHAT.DOUBLE
      self.stepper.step(steps, direction, style)

  # Converts degrees to a number of steps
  def degrees(self, degrees, direction=0):
    self.step(1-direction, int(round(0.556*degrees)))

  # Start the stepper thread
  def run(self, direction = 0, lim = None):
    if(ON_PI):
      self.done = True
      while (self.st1.isAlive()):
        time.sleep(0.010)
      self.st1 = threading.Thread(target=self.stepper_worker, args=(direction, Adafruit_MotorHAT.DOUBLE, lim))
      self.st1.start()      

  # Stepper thread
  def stepper_worker(self, direction, style, lim = None):
    self.done = False
    if(self.invert):
      direction = 1 - direction
    if(ON_PI):
      if(lim == None):
        while(not self.done):
          self.step(direction, 1, style)
      else:
        while(not self.done):
          self.step(direction, 1, style)
          if(not lim.getState()):
            self.done = True
    else:
      self.done = True
    self.release()

  # Test function to randomly increment stepper motor
  def test(self):
    while (True):
      if not self.st1.isAlive():
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
        self.st1 = threading.Thread(target=self.stepper_worker, args=(self.stepper, randomsteps, dir, stepstyles[random.randint(0,3)],))
        self.st1.start()
  
  # Check if the motor is currently moving
  def isMoving(self):
    return not self.done
