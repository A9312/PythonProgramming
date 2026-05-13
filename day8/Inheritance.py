
class A:
    def m1(self):
        print("this is m1 method from class A")

class B(A):
    def m2(self):
        print("this is m2 method from class B")

bobj=B()

bobj.m1()

bobj.m2()


class A:
    x,y=10,30
    def m1(self):
        print(self.x+self.y)

class B(A):
    a,b=100,300
    def m2(self):
        print(self.b-self.a)


bobj=B()

bobj.m1()

bobj.m2()



class A:
    a,b=10,20
    def m1(self):
        print(self.a+self.b)

class B(A):
    c,d=20,10
    def m2(self):
        print(self.c-self.d)


class C(B):
    e,f=20,30
    def m3(self):
        print(self.e*self.f)


cobj=C()

cobj.m1()

cobj.m2()

cobj.m3()


class A:
    a,b=10,20
    def m1(self):
        print(self.a+self.b)


class B(A):
    c,d=20,10
    def m2(self):
        print(self.c-self.d)

class C(A):
    e,f=20,40
    def m3(self):
        print(self.e*self.f)

cobj=C()

cobj.m1()

# cobj.m2()  bcz c extends only A

cobj.m3()


class A:
    a,b=10,20
    def m1(self):
        print(self.a+self.b)

class B:
    c,d=30,40
    def m2(self):
        print(self.d-self.c)

class C(A,B):
    e,f=30,40
    def m3(self):
        print(self.e*self.f)


cobj=C()

cobj.m1()

cobj.m2()

cobj.m3()


class A:
    def m1(self):
        print("this is m1 method from class A")

class B(A):
    def m1(self):
        print("this is m1 method from class B")

bobj=B()

bobj.m1()


class A:
    def m1(self):
        print("this is m1 method from class A")


class B(A):
    def m1(self):
        print("this is m1 method from class B")
        super().m1()

bobj=B()

bobj.m1()


class A:
    a,b=20,30


class B(A):
    i,j=10,20
    def m(self,x,y):
        print(x+y)
        print(self.i+self.j)
        print(self.a+self.b)

bobj=B()

bobj.m(10,90)

class A:
    name="john"

class B(A):
    name = "cena"

bobj=B()

print(bobj.name)

print(super(B,bobj).name)




class Bank:
    def rateofinterest(self):
        return 0


class HDFC(Bank):
    def rateofinterest(self):
        return 10

class ICICI(Bank):
    def rateofinterest(self):
        return 12

hdfc=HDFC()
print(hdfc.rateofinterest())

icici=ICICI()
print(icici.rateofinterest())

class Human:
    def hello(self,name=None):
        if name is not None:
            print("hello "+name)
        else:
            print("hello")

h=Human()

h.hello("john")

h.hello()

class calculation:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)

c=calculation()

c.add(10,20,30)
























