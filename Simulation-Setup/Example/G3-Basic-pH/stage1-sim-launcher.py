import os
import sys

import shutil

import subprocess
import string


## Read input parameters 
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
print("What is the generation?:" + str(args[0]) + "\n")
print("Name of Base folder:" + str(args[1]) + "\n")
print("Data Points:" + str(args[2]) + "\n")
############################################


source = os.getcwd()       
target="PARENT"

test_desktop_script="Desktop_run.bash"
Slurm_script="run_slurm.bash"


name = input('Type 1 for Desktop testing, and 2 for production on hpc:')  

if int(name) == 1:
    use_script=test_desktop_script
elif int(name) == 2:
    use_script=Slurm_script 



exec_arg_1 = "./" + use_script

datapoints_1 = args[3].split(',')
datapoints_2 = args[5].split(',')

for x in range(len(datapoints_1)): 

    output = args[0] + '_'+ datapoints_1[x] + ".int" 
    out1 = open(output, "w") 
    out1.writelines("1.What is the generation?" + '\t' + str(args[0]) + '\n')
    out1.writelines("2.What is the name of the base file?" + '\t' + str(args[1]) + '\n')
    out1.writelines("3.Number of data points" + '\t' + '1' + '\n')
    out1.writelines("4.Grid spacing" + '\t' + str(datapoints_1[x]) + '\n')
    out1.writelines("5.ions per dendron" + '\t' + str(args[4]) + '\n')
    out1.writelines("6.Relaxation gap" + '\t' + str(datapoints_2[x]) + '\n')
    out1.close()
    
    try:
        shutil.copy(source + '/' + output, source + '/' + target)
        subprocess.check_call(["rm", output])
        os.chdir(source + '/' + target)
        
        subprocess.check_call(["tar", "xvf", args[1] + ".tar.gz"])
        subprocess.check_call([exec_arg_1, output, args[1], args[0]])
        
        os.chdir(source)
            
    except Exception:
        pass
        
    
###########################################################


    
