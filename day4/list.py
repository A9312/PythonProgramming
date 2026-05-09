
mylist1=[1,2,3,4,5,6,7]

mylist2=["banana","apple","mango"]

mylist3=["macbook",10,"windows",20,"linux",30]

mylist4=list()


print(mylist1)

print(mylist2)
print(mylist3)
print(mylist4)


print(mylist1[1])

print(mylist1[2:5])

mylist=["apple","mango","cherry"]

mylist[0]="orange"

print(mylist)

for i in mylist:
    print(i)


mylist5=[10,20,40,332,46,9852,273482,94]

search_element=9852

for i in mylist5:
    print(i)
    if search_element==i:
        break

print("end program")

print(len(mylist5))

mylist6=["apple","mango","cherry"]
mylist6.append("banana")
print(mylist6)

mylist6.insert(2,"orange")
print(mylist6)

mylist6.pop(2)
print(mylist6)

del mylist6[2:4]
print(mylist6)

mylist6.clear()
print(mylist6)

mylist7=[10,20,40,332,46,9852,273482,94]
mylist8=list(mylist7)
print(mylist7)
print(mylist8)

mylist9=mylist7.copy()
print(mylist9)

mylist1=[1,2,3]
mylist2=['a','b','c']
mylist3=mylist1+mylist2
print(mylist3)

for i in mylist2:
    mylist1.append(i)
print(mylist1)

mylist1=[1,2,3]
mylist2=['a','b','c']
mylist2.extend(mylist1)
print(mylist2)
