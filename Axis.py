# Axis Object Declaration
from Limit_Switch import LimitSwitch

class Axis:
  def __init__(self):
    self.motors = []
    return
    
  def attach(self, motor, LimitSwitchHome, LimitSwitchEnd):
    self.motors.append({'motor': motor, 'limitSwitchHome': LimitSwitchHome, 'limitSwitchEnd': LimitSwitchEnd})
#    self.motors[-1]['limitSwitchHome'].setCallback(self.motors[-1]['motor'].stop)
#    self.motors[-1]['limitSwitchEnd'].setCallback(self.motors[-1]['motor'].stop)
    
  def printMotorAttachments(self):
    print "Current Motors Attached: "
    print self.motors
    
  def homeAxis(self):
    self.move(0)

  def atHome(self):
    home = False
    for i in range(len(self.motors)):
      home = not self.motors[i]['limitSwitchHome'].getState()
      if home:
        break
    return home

  def move(self,direction = 0):
    for i in range(len(self.motors)):
      if(direction == 0 and self.motors[i]['limitSwitchHome'].getState()):
        self.motors[i]['motor'].run(0, self.motors[i]['limitSwitchHome'])
      elif(direction == 1 and self.motors[i]['limitSwitchEnd'].getState()):
        self.motors[i]['motor'].run(1, self.motors[i]['limitSwitchEnd'])

  def stop(self):
    for i in range(len(self.motors)):
      self.motors[i]['motor'].stop()
