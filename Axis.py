# Axis Object Declaration
from Limit_Switch import LimitSwitch

class Axis:
  def __init__(self):
    self.motors = []
    return
    
  # Attach a motor and limit switches to an axis
  def attach(self, motor, LimitSwitchHome, LimitSwitchEnd):
    self.motors.append({'motor': motor, 'limitSwitchHome': LimitSwitchHome, 'limitSwitchEnd': LimitSwitchEnd})
  
  # Print the motors and limit switches that are attached to this axis
  def printMotorAttachments(self):
    print "Current Motors Attached: "
    print self.motors
    
  # Move the axis to its home position
  def homeAxis(self):
    self.move(0)

  # Check if all motors are at the home position
  def atHome(self):
    home = False
    for i in range(len(self.motors)):
      if (self.motors[i]['limitSwitchHome'] == None):
        continue
      home = not self.motors[i]['limitSwitchHome'].getState()
      if home:
        break
    return home

  # Move the axis
  def move(self,direction = 0):
    for i in range(len(self.motors)):
      if(direction == 0 and self.motors[i]['limitSwitchHome'] == None):
        self.motors[i]['motor'].run(0, self.motors[i]['limitSwitchHome'])
      elif(direction == 1 and self.motors[i]['limitSwitchEnd'] == None):
        self.motors[i]['motor'].run(1, self.motors[i]['limitSwitchEnd'])
      elif(direction == 0 and self.motors[i]['limitSwitchHome'].getState()):
        self.motors[i]['motor'].run(0, self.motors[i]['limitSwitchHome'])
      elif(direction == 1 and self.motors[i]['limitSwitchEnd'].getState()):
        self.motors[i]['motor'].run(1, self.motors[i]['limitSwitchEnd'])

  # Stop the axis motion
  def stop(self):
    for i in range(len(self.motors)):
      self.motors[i]['motor'].stop()
      
  # Is the axis moving?
  def isMoving(self):
    moving = False
    for i in range(len(self.motors)):
      moving |= (self.motors[i]['motor'].isMoving())
    return moving