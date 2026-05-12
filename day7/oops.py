
class Myclass:
    def func(self):
        pass
    def display(self):
        print("john")


m1=Myclass()

m1.func()

m1.display()

class Myclass:
    def func(self):
        pass
    def display(self,name):
        print(name)

m1=Myclass()

m1.func()

m1.display("john")

class Myclass:
    def m1(self):
        print("this is an instance method")
    @staticmethod
    def m2(self,num):
        print(self,num)

m3=Myclass()

m3.m1()

m3.m2(100,200)


class Myclass:
    def m1(self):
        print("this is an instance method")
    @staticmethod
    def m2(self,num):
        print(self,num)

Myclass.m2(100,200)


class Myclass:
    a,b=10,20   #class variables
    def add(self):
        print(self.a+self.b)
    def mul(self):
        print(self.a*self.b)

m1=Myclass()

m1.add()

m1.mul()

a,b=10,20

class Myclass:
    c,d=30,40
    def add(self,x,y):
        print(x+y)
        print(self.c+self.d)
        print(a,b)

m1=Myclass()

m1.add(200,400)


a,b=10,20

class Myclass:
    a,b=30,40
    def add(self,a,b):
        print(a+b)
        print(self.a+self.b)
        print(globals()['a']+globals()['b'])

m1=Myclass()

m1.add(10,20)


class Myclass:
    def display(self,name):
        print("this is display method")
        print(name)

obj1=Myclass()

obj1.display("john")


obj2=Myclass()

obj2.display("john")


class Myclass:
    def __init__(self):
        print("this is an constructor")
    def m1(self):
        print("hello..")
    def m3(self,x,y):
        return(x+y)

m2=Myclass()

print(m2.m3(10,20))








