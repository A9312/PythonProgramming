from importlib.metadata import files

file=open("/Users/shreygupta/Downloads/Self/Akshit/testfile.txt",'w')
file.write("this is my first statement\n")
file.write("this is my second statement\n")
file.write("this is my third statement\n")
file.write("this is my fourth statement\n")

file.close()

print("program is closed")

file=open("/Users/shreygupta/Downloads/Self/Akshit/testfile.txt",'r')

print(file.read())

file.close()

file=open("/Users/shreygupta/Downloads/Self/Akshit/testfile.txt",'a')

file.write("this is my fifth line")

file.close()


