

def func(i,j):
    print(i,j)

func(10,20)


def func(i,j=10):
    print(i,j)

func(100,200)

def func(i,j=10):
    print(i,j)

func(100)

def greetings(name,greeting):
    print(greeting+" "+name)

greetings(name="john",greeting="hello")

def fun(a,b,c):
    print(a,b,c)

fun(10,30,20)

fun(a=10,b=20,c=30)

fun(10,30,c=20)

# fun(a=10,20,c=30) #this is wrong because positional argument must appear before any keyword argument

def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a

print(largest(30,20))




