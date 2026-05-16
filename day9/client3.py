
import sys

sys.path.append("/Users/shreygupta/PycharmProjects/PythonProgramming/day9/packages1")
sys.path.append("/Users/shreygupta/PycharmProjects/PythonProgramming/day9/packages2")

import emp_module

import stu_module

obj1=emp_module.employee()

obj1.disemp()

obj2=stu_module.student()

obj2.dispstu()