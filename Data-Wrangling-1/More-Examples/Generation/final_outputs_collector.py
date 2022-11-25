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
    
    for filename in os.listdir(os.getcwd()):
    
        seed_dir = conc_dir + '/' + str(filename)
        analysis_output_dir = seed_dir  + '/' + analysis_direc + '/' + "Outputs"
        
        isExist = os.path.exists(analysis_output_dir)
        if isExist:
        
            os.chdir(seed_dir)    
            
            path_combinedoutputs = seed_dir + '/' + combinedoutputs
            isExist = os.path.exists(path_combinedoutputs)
            
            if not isExist:
                subprocess.check_call(['mkdir', combinedoutputs])
            
            os.chdir(analysis_output_dir) 
            
            for outfilename in os.listdir(os.getcwd()):
            
                try:
                    shutil.copy(outfilename, path_combinedoutputs)
                except Exception:
                    pass
             
        os.chdir(conc_dir)

#############################################################################################



