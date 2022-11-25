file = open("system.top", "r")
line_count = 0
for line in file:
    line_count += 1
       
file.close()


file1 = open("system_dummy.top", "r")


for line1 in reversed(list(file1)):


    with open("system.top", "r") as f:
        contents = f.readlines()

    contents.insert(line_count-1, line1 + "\n")


    with open("system.top", "w") as f:
        contents = "".join(contents)
        f.write(contents)
        
file1.close()
        
