import os
import sys

import shutil

import subprocess


###########################################
arguments = len(sys.argv) - 1
inputfilename = sys.argv[1]
# output argument-wise
f = open(inputfilename, "r")
lines = f.readlines()
args = []
for x in lines:
    args.append(x.split('\t')[1].strip())
f.close()

########################################


print("What is the generation? \n")

input1 = args[0]

print("What is the name of the base file? \n")

input2 = args[1]

# creating an empty list
lst = []
 
# number of elements as input
n = int(args[2])
 
# iterating till the range
for i in range(0, n):
    print("Grid spacing for %i data point" %(i))
    ele = int(args[3])
    
    lst.append(ele) # adding the element
     
print(lst)

ionsperden=int(args[4])

gap=float(args[5])

griding=0

for items in lst:
    
    
    actual_grid=items+1
    griding=(actual_grid*actual_grid)*2
     
    print("Current directory :", os.getcwd())
    
    basedirectory=os.getcwd()
    
    source= os.getcwd()+'/'+input2

    destination= os.getcwd()+'/'+ input1+ '_'+ str(griding)


    print(int(items))
    shutil.copytree(source, destination)
    
    os.chdir(destination)
    
    
    
    subprocess.check_call(['./parent_modeling.bash', str(items),str(ionsperden), str(gap)])
    
    os.chdir(basedirectory)

