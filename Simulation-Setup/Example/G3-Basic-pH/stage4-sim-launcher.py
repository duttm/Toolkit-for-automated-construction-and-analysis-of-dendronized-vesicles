import os
import sys

import shutil

import subprocess
import string

###########################################################################################################

def getDirectoryList(path,target_file):
    directoryList = []

    #return nothing if path is a file
    if os.path.isfile(path):
        return []

    #add dir to directorylist if it contains .txt files
    if len([f for f in os.listdir(path) if f.endswith(target_file)])>0:
        directoryList.append(path)

    for d in os.listdir(path):
        new_path = os.path.join(path, d)
        if os.path.isdir(new_path):
            directoryList += getDirectoryList(new_path,target_file)

    return directoryList
###############################################################################################################3    

directory = "Vesicle_Prod"

target_file = "20-input.gro"
    
source = os.getcwd()       
target="PARENT"

list = getDirectoryList(source + '/' + target, target_file)

test_interactive_script="just.bash"
Slurm_script="gromacs_prod.job"


name = input('Type 1 for interactive testing, and 2 for production:')  

if int(name) == 1:
    use_script=test_interactive_script
    exec_arg_1 = "./" + use_script
elif int(name) == 2:
    use_script=Slurm_script
    exec_arg_1 = use_script 


arguments = len(sys.argv) - 1
Generation = sys.argv[1]
ITP = sys.argv[2]
TOP = sys.argv[3]

for i in range(len(list)): 

    if Generation in list[i]:
        ##print(list[i])
        try:
            shutil.copy(source + '/' + directory + ".tar.gz", list[i])
            ##subprocess.check_call(["rm", output])
            os.chdir(list[i])
        
            subprocess.check_call(["tar", "xvf", directory + ".tar.gz"])
            ##os.chdir(list[i])
            
            shutil.copy(list[i] + '/' + ITP, list[i] + '/' + directory)
            shutil.copy(list[i] + '/' + TOP, list[i] + '/' + directory)
            shutil.copy(list[i] + '/' + target_file, list[i] + '/' + directory)
            
            os.chdir(list[i] + '/' + directory)
            
            if int(name) == 1:
                subprocess.check_call([exec_arg_1])
            elif int(name) == 2:
                subprocess.check_call(["sbatch", exec_arg_1])


            
            
            
            os.chdir(source)
        
            
            
        except Exception:
            pass
        
        
    else:
        print("Not found")


