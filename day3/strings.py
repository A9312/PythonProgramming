

s="welcome"

a='welcome'

b=str("welcome")

c=str('welcome')


#creating empty string variable

name=" "

name=' '

name=str()

#Strings are immutable

str1="welcome"

print(id(str1))

str1=str1+" to python"

print(str1)

str1="welcome to "

print(str1+" programming")

print(str1*5)


#slicing []

a="welcome"

print(a[1:3])

print(a[:5])

print(a[1:-1])

print(ord('A')) #returns ascii value

print(chr(65)) #returns ascii character

print(max('abc'))

print(min('abc'))

print(len('abc'))


s="welcome"

print("come" in s)

print("time" in s)

print("time" not in s)

print("time" == "tim")

print("free" != "freedom")

print("arrow" > "aron")

print("right" >= "left")

print("teeth" < "tee")

print("yellow" <= "fellow")

print("abc" > " ")

s="welcome to python"

print(s.isalnum())

print(s.isalpha())

print("2013".isdigit())

print("first number".isidentifier())

print(s.islower())

print(s.isupper())

print(" ".isspace())


s="welcome to python"

print(s.endswith("thon"))

print(s.startswith("good"))

print(s.find("come"))

print(s.find("become"))

print(s.count("t"))


s="Strings in PYTHON"

print(s.capitalize())

print(s.title())

print(s.upper())

print(s.lower())

print(s.swapcase())

print(s.replace("ri","ab"))



s="welcome"
rev_str=""

for i in s:
    rev_str = i + rev_str
print(rev_str)

s="welcome"
rev_str=s[::-1]
print(rev_str)