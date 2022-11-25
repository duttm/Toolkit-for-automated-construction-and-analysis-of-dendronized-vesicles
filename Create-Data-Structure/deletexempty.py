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
    
    
    if filename.find("_")!=-1:
    
        x = filename.split('_')[1].strip()
        conc.append(x.split('-')[0].strip())
        seed.append(x.split('-')[1].strip())
        nameofdir.append(filename)
        
            
source = os.getcwd()       
analysis_direc = "Analysis_G4_Basic_2" 
final_analysis_name = "Analysis_G4_2" 
destination = "/mantel/abanerjee/DL-PH/DATA/BASIC/G4"
       
print(os.getcwd())

##########################################################################################

for i in range(len(conc)):


    destination_directory = destination + '/' + conc[i]
    
    for j in range(11):
    
        ultimate = destination_directory + '/' + "s" + str(j)
        isExist = os.path.exists(ultimate)
        if isExist:
            dir = os.listdir(ultimate)
            if len(dir) == 0:
                print(ultimate + " is Empty" + '\n')
                shutil.rmtree(ultimate)
    
##########################################################################################
    
    
##########################################################################################

for i in range(len(conc)):


    destination_directory = destination + '/' + conc[i]     
    isExist = os.path.exists(destination_directory)
    if isExist:
        dir = os.listdir(destination_directory)
        if len(dir) == 0:
            print(destination_directory + " is Empty" + '\n')
            shutil.rmtree(destination_directory)
    
##########################################################################################
    
    

