import os
import sys

import shutil

import subprocess
import string
##from distutils.dir_util import copy_tree

#################################################################################

##arguments = len(sys.argv) - 1
generation = "G5"
ph = "ACIDIC"
margin = "1.6"
vmd= "G1_vesicle.vmd"

analysis_dir = "image_render_" + generation
analysis_file = analysis_dir + ".tar.gz"
random_file = "vmd_dom.bash" 



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


exec_arg_1 = "./" + random_file
exec_arg_2 = "*.gro"
exec_arg_3 = "*.xtc"

    

##########################################################################################


#for i in range(1):
for i in range(len(conc)):
    
    conc_dir = source + '/' + str(conc[i])
    os.chdir(conc_dir)
    counter = 0
    for filename in os.listdir(os.getcwd()):
        
        analysis = conc_dir + '/' + filename
        
        os.chdir(analysis)
        
        image_name = generation + '_'+ ph + '_' + str(conc[i])
        
        
        try:
            shutil.copy(source + '/' + analysis_file, analysis)
            shutil.copy(source + '/' + random_file, analysis)
            
            #subprocess.check_call([exec_arg_1, exec_arg_2, exec_arg_3, margin, vmd, image_name])
            
        except Exception:
            pass
            
        try:
            ##shutil.copy(source + '/' + analysis_file, analysis)
            ##shutil.copy(source + '/' + random_file, analysis)
            
            subprocess.check_call([exec_arg_1, exec_arg_2, exec_arg_3, margin, vmd, image_name, analysis_dir])
            
        except Exception:
            pass

            
        

     
     
#############################################################################################
os.chdir(source)


