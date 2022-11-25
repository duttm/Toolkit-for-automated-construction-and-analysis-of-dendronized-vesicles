filename="DEN.gro"

fp = open(filename)
line_count = 0

for i, line in enumerate(fp):
    if i == 1:
        a = int(line.strip())
        break
fp.close()

inputfilename="center_index_number.txt"

f = open(inputfilename, "r")
lines = f.readlines()
args = []
for x in lines:
    args.append(x.split('\t')[1].strip())
    f.close()

b = args[0]
c= int(a)+int(b)

print(int(a)+int(b))

file_object = open('index_mod.ndx', 'a') ## try to pass index file name from bash
file_object.write("[center]"+'\n')
file_object.write(str(c)+'\n')
file_object.close()

