
myset={"apple","mango","orange"}

print(myset)

myset={"apple","mango","orange"}

for i in myset:
    print(i)

myset={"apple","mango","orange"}

print("banana" in myset)

print("mango" in myset)

myset={"apple","mango","orange"}

myset.add("cherry")

print(myset)

myset={"apple","mango","orange"}

myset.update(["cherry","banana"])

print(myset)

myset={"apple","mango","orange"}

myset.remove("apple")

print(myset)

myset={"apple","mango","orange"}

print(len(myset))

myset={"apple","mango","orange"}

myset.remove("apple")

print(myset)

myset={"apple","mango","orange"}

myset.discard("apple")

print(myset)

myset={"apple","mango","orange"}

myset.clear()

print(myset)

myset={"apple","mango","orange"}

# del myset

print(myset)

set1={1,2,3}

set2={"a","b","c"}

set3=set1.union(set2)

print(set3)

set1={1,2,3}

set2={"a","b","c"}

set1.update(set2)

print(set1)