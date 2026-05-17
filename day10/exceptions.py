

print("this is starting point of program")
print("this is starting point of program")
print("this is starting point of program")

try:
    print(x)
except:
    print("exception occured")

print("this is the end of program")

print("this is starting of program")

print("program is in progress")

try:
    print(10/0)
except ZeroDivisionError:
    print("program completed")

print("program completed")

try:
    num1,num2=10,0

    result=num1/num2

    print("result is:",result)

except ZeroDivisionError:
    print("thrown ZeroDivisionError exception")

except SyntaxError:
    print("thrown syntax error exception")

except:
    print("exception handled")

else:
    print("no exception occured")

finally:
    print("always execute")


def enterage(num):
    if num<0:
        raise ValueError("Only Integers are allowed")
    if num%2==0:
        print("even")
    else:
        print("odd")



num=-1

try:
    enterage(num)
except ValueError:
    print("ValueError exception occured and handled")

print("program completed")





















