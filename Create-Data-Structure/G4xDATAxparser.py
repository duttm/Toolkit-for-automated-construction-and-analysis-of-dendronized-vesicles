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
    isExist = os.path.exists(destination_directory)
    if not isExist:
            
        os.chdir(destination)    
        subprocess.check_call(['mkdir', conc[i]])
        
        os.chdir(destination_directory)
        subprocess.check_call(['mkdir', 's0', 's1', 's2', 's3', 's4', 's5', 's10'])
        os.chdir(source)
                


#############################################################################################


for i in range(len(conc)):

        path_back = os.getcwd() + '/' + nameofdir[i]
        path = os.getcwd() + '/' + nameofdir[i] + '/' + analysis_direc
        destination_directory = destination + '/' + conc[i]

        isExist = os.path.exists(path)
 
        if isExist:
            os.chdir(path)
            
            print(os.getcwd())
           
            inputfilename = "output.out"
            f = open(inputfilename, "r")
            lines = f.readlines()[0:2]
            store = []
            for x in lines:
                store.append(x.split(' ')[0].strip())
            f.close()
            print(store[0],store[1])
            
            print("Reading files in" + ' ' + path_back + '\n')
            
            ultimate = destination_directory + '/' + seed[i]
            ultimate_ana_dir = destination_directory + '/' + seed[i] + '/' + final_analysis_name
            
            gro = path_back + '/' + store[0]
            xtc = path_back + '/' + store[1]
            
            shutil.copy(gro, ultimate)
            shutil.copy(xtc, ultimate)
            shutil.copytree(path, ultimate_ana_dir)
            
            os.chdir(source)
            

            
            

###################################################################################



