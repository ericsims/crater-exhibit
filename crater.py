# Crater Maker Exhibit

from Axis import Axis
from Limit_Switch import LimitSwitch
import platform
import yaml

system = platform.system() + " " + platform.release()
print system
f = open('settings.yaml')
settings = yaml.safe_load(f)
f.close()

x = Axis()
x.attach(settings['StepperHat']['addr'][0], LimitSwitch(0), 0)
x.attach(settings['StepperHat']['addr'][0], LimitSwitch(1), 1)
x.printMotorAttachments()