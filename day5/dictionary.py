
mydict={101:"a",102:"b",103:"c"}

print(mydict)

mydict={
    "brand":"mercedes",
    "model":"gwagon",
    "year":2026
}

print(mydict["brand"])

print(mydict["model"])

print(mydict["year"])

mydict={
    "brand":"mercedes",
    "model":"gwagon",
    "year":2026
}

print(mydict.get("brand"))

mydict={
    "brand":"mercedes",
    "model":"gwagon",
    "year":2026
}

mydict["year"]=2021

print(mydict.get("year"))

mydict={
    "brand":"mercedes",
    "model":"gwagon",
    "year":2026
}

for i in mydict:
    print(i)

mydict={
    "brand":"mercedes",
    "model":"gwagon",
    "year":2026
}

for i in mydict:
    print(mydict[i])

mydict={
    "brand":"mercedes",
    "model":"gwagon",
    "year":2026
}

for i in mydict.values():
    print(i)


mydict={
    "brand":"mercedes",
    "model":"gwagon",
    "year":2026
}

for x,y in mydict.items():
    print(x,y)


mydict={
    "brand":"mercedes",
    "model":"gwagon",
    "year":2026
}

print(len(mydict))


mydict={
    "brand":"mercedes",
    "model":"gwagon",
    "year":2026
}

mydict["color"]="black"

print(mydict)

mydict={
    "brand":"mercedes",
    "model":"gwagon",
    "year":2026
}

mydict.pop("year")

print(mydict)

mydict={
    "brand":"mercedes",
    "model":"gwagon",
    "year":2026
}

del mydict["year"]

print(mydict)

mydict={
    "brand":"mercedes",
    "model":"gwagon",
    "year":2026
}

del mydict

# print(mydict)

mydict={
    "brand":"mercedes",
    "model":"gwagon",
    "year":2026
}

mydict.clear()

print(mydict)

mydict1={
    "brand":"mercedes",
    "model":"gwagon",
    "year":2026
}

mydict2=mydict1

print(mydict2)

mydict1={
    "brand":"mercedes",
    "model":"gwagon",
    "year":2026
}

mydict2=mydict1.copy()

print(mydict2)