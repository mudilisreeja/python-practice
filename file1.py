f = open("test.txt", "w")
f.write("hello i am learning python")

###########
with open("test.txt", "r") as f:
    data = f.read()
new_data = data.replace("hello", "hi")
print(new_data)
