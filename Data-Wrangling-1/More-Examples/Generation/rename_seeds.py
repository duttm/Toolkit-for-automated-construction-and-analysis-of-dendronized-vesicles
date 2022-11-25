import os
import sys

import shutil

import subprocess
import string
##from distutils.dir_util import copy_tree

analysis_direc = sys.argv[1]
combinedoutputs = sys.argv[2]

######################################################################################

conc = []
seed = []
nameofdir = []


for filename in os.listdir(os.getcwd()):
    
    if not filename.find("_") != -1:
        conc.append(filename)
        
####################################################################################        
            
source = os.getcwd()       

       

##########################################################################################

for i in range(len(conc)):
    
    conc_dir = source + '/' + str(conc[i])
    os.chdir(conc_dir)
    
    print("We are in:" + os.getcwd() + '\n')
    
    counter = 0
    for filename in os.listdir(os.getcwd()):
        
        
        newname = "c" + str(counter)
        subprocess.check_call(['mv', filename, newname])
        counter = counter + 1

#############################################################################################



