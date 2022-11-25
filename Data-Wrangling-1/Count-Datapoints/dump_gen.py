import os
import sys

import shutil

import subprocess
import string
##from distutils.dir_util import copy_tree


analysis_direc = sys.argv[1]
combinedoutputs = sys.argv[2]
nameofana = sys.argv[3]
generation = sys.argv[4]

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


file_out = open(generation + ".txt", "w")       

##########################################################################################

for i in range(len(conc)):
    
    conc_dir = source + '/' + str(conc[i])
    os.chdir(conc_dir)
    counter = 0
    for filename in os.listdir(os.getcwd()):
        
        analysis = conc_dir + '/' + filename + '/' + combinedoutputs + '/' + nameofana
        isExist = os.path.exists(analysis)
        if isExist:    
            counter = counter + 1
    
    if counter != 0:
        file_out.writelines(str(conc[i]) + ' ' + str(counter) + '\n')    
   
#############################################################################################

file_out.close()

