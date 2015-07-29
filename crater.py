# Crater Maker Exhibit

from Axis import Axis
from Limit_Switch import LimitSwitch
import platform
import yaml

if(platform.system() == "Linux"):
  ON_PI = 1
else:
  print "\nWARNING: Not on Raspberry Pi\n"
  ON_PI = 0

f = open('settings.yaml')
settings = yaml.safe_load(f)
f.close()

x = Axis()
x.attach(settings['StepperHat']['addr'][0], LimitSwitch(0), 0)
x.printMotorAttachments()