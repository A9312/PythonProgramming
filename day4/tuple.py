
mytuple=("apple","mango","cherry")

print(mytuple)

print(mytuple[1])

print(mytuple[0:2])

mytuple=("apple","mango","cherry")

mylist=list(mytuple)

mylist[0]="orange"

mytuple=tuple(mylist)

print(mytuple)

mytuple=("apple","mango","cherry")

for i in mytuple:
    print(i)

mytuple=("apple","mango","cherry")
for i in mytuple:
    print(i)
    if i=="mango":
        break
print("end program")

mytuple=("apple","mango","cherry")

print(len(mytuple))

mytuple1=("apple","mango","cherry")

mytuple2=mytuple1

print(mytuple1)
print(mytuple2)

del mytuple2

# print(mytuple2)

mytuple1=("apple","mango","cherry")

mytuple2=(1,2,3)

mytuple3=mytuple1+mytuple2

print(mytuple3)

if mytuple1==mytuple2:
    print("tuples are equal")
else:
    print("tuples are not equal")