
import sys
from pickletools import dis

sys.path.append("/Users/shreygupta/PycharmProjects/PythonProgramming/day9/package1")

sys.path.append("/Users/shreygupta/PycharmProjects/PythonProgramming/day9/package1/package2")

import module1

module1.display()

import module2

module2.show()

from module1 import *

from module2 import *

display()

show()



