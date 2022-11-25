import os
import sys

import shutil

import subprocess
import string
##from distutils.dir_util import copy_tree

######################################################################################

conc = []
seed = []
nameofdir = []


for filename in os.listdir(os.getcwd()):
    
    if not filename.find("_") != -1:
        conc.append(int(filename.strip()))
        
        
conc.sort()        
####################################################################################        
            
source = os.getcwd()       
analysis_file = "Analysis_G1_3.tar.gz"
random_file = "ran_dom.bash" 

exec_arg_1 = "./" + random_file
exec_arg_2 = "*.gro"
exec_arg_3 = "*.xtc"

    

##########################################################################################

for i in range(len(conc)):
    
    conc_dir = source + '/' + str(conc[i])
    os.chdir(conc_dir)
    counter = 0
    for filename in os.listdir(os.getcwd()):
        
        analysis = conc_dir + '/' + filename
        
        os.chdir(analysis)
        
        try:
            shutil.copy(source + '/' + analysis_file, analysis)
            shutil.copy(source + '/' + random_file, analysis)
            subprocess.check_call([exec_arg_1, exec_arg_2, exec_arg_3])
            
        except Exception:
            pass
     

#############################################################################################
os.chdir(source)


