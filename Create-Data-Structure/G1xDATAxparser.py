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
    
    
    if filename.find("_")!=-1 and filename.find("-")!=-1:
    
        x = filename.split('_')[1].strip()
        conc.append(x.split('-')[0].strip())
        seed.append(x.split('-')[1].strip())
        nameofdir.append(filename)
        
            
source = os.getcwd()       
analysis_direc = "Analysis_G1_3" 
final_analysis_name = analysis_direc
destination = "/mantel/abanerjee/DL-PH/DATA/BASIC/G1"
inputfilename = "G2.err"

       
##print(os.getcwd())

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
            
            ##print(os.getcwd())
            
            store = []
        
            ##########################

            # opening a text file
            
            for k in range(20,40):
                grostring = str(k) +'-input.gro'
                file1 = open(inputfilename, "r")
                
                readfile = file1.read()
                
                if grostring in readfile: 
                    ##print('String', grostring, 'Found In File')
                    store.append(grostring)
                    break 
           
  

                file1.close() 

            
            ###############################
            
            for k in range(20,40):
                xtcstring = str(k) +'-input.xtc'
                file1 = open(inputfilename, "r")
                
                readfile = file1.read()
                
                if xtcstring in readfile: 
                    ##print('String', xtcstring, 'Found In File')
                    store.append(xtcstring)
                    break 
          
  

                file1.close() 
            
            ##########################
            


            
            ###############################
            print(len(store))
            if len(store) == 2:
            
                ##print(store[0],store[1])
            
            #########################################3
            
            
                ##print("Reading files in" + ' ' + path_back + '\n')
            
                ultimate = destination_directory + '/' + seed[i]
                ultimate_ana_dir = destination_directory + '/' + seed[i] + '/' + final_analysis_name
            
                gro = path_back + '/' + store[0]
                xtc = path_back + '/' + store[1]
            
                try:
                   
                   
                    print('\n' + "coping:" + '\n' + str(gro) + '\n' + str(xtc) + '\n' + 'to' +  '\n' + str(ultimate) + '\n')   
                    shutil.copy(gro, ultimate)
                    shutil.copy(xtc, ultimate)
                    shutil.copytree(path, ultimate_ana_dir)
                except Exception:
                    pass
                    
        
            os.chdir(source)


###################################################################################

###Delete code#################################################################

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

