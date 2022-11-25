import os
import sys

import shutil

import subprocess
import string
##from distutils.dir_util import copy_tree

#################################################################################

arguments = len(sys.argv) - 1
generation = sys.argv[1]
ph = "ACIDIC"
margin = "1.2"
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
        
        extension = analysis_dir + '/' + 'IMAGE'
        
        
        os.chdir(analysis + '/' + extension)
        
        file_exists = os.path.exists(analysis + '/' + extension + '/' + "write_0.gro")
        
        print(str(file_exists) + " " + analysis + '/' + extension)
        


        

     
     
#############################################################################################
os.chdir(source)


