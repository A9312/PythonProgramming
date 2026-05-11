

global_var = 20

def func():
    local_var=10
    print(local_var)
    print(global_var)

func()

xy=100

def funce():
    xy=200
    print(xy)

funce()

xy=100

def func():
    global xy
    xy=200
    print(xy)

func()

x=100

def func():
    global x
    x=300
    print(x)

func()

print(x)

def func():
    global x
    x=100
    print(x)

func()

print(x)


