f = open("sample.txt", "r")
data = f.read()
print(data)
f.close()
######
f = open("sample.txt", "w")
data = f.write("This is my new file")
f.close()
##########3
f = open("sample.txt", "a")
f.write("I created first time")
f.close()
############
f = open("file1.txt", "w")
data1 = f.write("hello")
f.close()
###########with syntax
with open("sample.txt", "r")as f:
     data2 = f.read()
     print(data2)




