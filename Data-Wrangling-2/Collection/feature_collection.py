import os
import sys

import shutil

import subprocess
import string
##


########################################################

arguments = len(sys.argv) - 1
Base_directory=sys.argv[1] + "/DATA"
PH= ["ACIDIC", "BASIC"]
FEATURE= ["ROG_DENS_TA", "TA-TA", "TA-PO4", "Den_layer_thickness", "DHS_TAbeads", "AND_results", "hydrophobic_vol", "packing_factor", "Thickness_Bilayer"]
GEN= ["G1", "G2", "G3", "G4", "G5", "G6"]



###################################


for i in range(len(PH)):
    for j in range(len(FEATURE)):
        for k in range(len(GEN)):

            Analysis = Base_directory + '/' +  PH[i] + '/' + FEATURE[j] + '/' + "Summary" + GEN[k] + ".txt"

            f2=open(Analysis,"r")
     
            name_file = GEN[k] + '_' + PH[i] + '_' + FEATURE[j] + '.txt'     
            
            file_out = open(name_file, "w")
            lines = f2.readlines()
            for x in lines:
                file_out.writelines(str(GEN[k]) +' '+ str(PH[i])  + ' ' +  str(x.split()[1].strip()) + ' ' + str(float(x.split()[2].strip())) + '\n' )
            f2.close()    

            file_out.close()

