file = open("system.top", "r")
line_count = 0
for line in file:
    line_count += 1
       
file.close()


with open("system.top", "r") as f:
    contents = f.readlines()

contents.insert(line_count-1, "Hi \n")
contents.insert(line_count-2, "Hi there \n")

with open("system.top", "w") as f:
    contents = "".join(contents)
    f.write(contents)
        

        
