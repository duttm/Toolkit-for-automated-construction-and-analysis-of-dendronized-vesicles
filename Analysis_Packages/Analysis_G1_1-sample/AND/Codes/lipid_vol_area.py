import numpy
from index import *

def pack_factor(array, upcount, LC, eff_rad_1_b, NOF, measureable, output_textfile):


    file_out = open(output_textfile, "w")

    file_out.writelines("Frame" + '\t' + measureable + '\n')
    
    hydrophobic_vol_whole = []
        
    for k in range(NOF):
    
        head_area = (4 * 3.14 * (array[k] ** 2)) / upcount[k]
        hydrophobic_vol = ((4/3) * 3.14 * ((eff_rad_1_b[k])**3 - (eff_rad_1_b[k] - LC[k])**3) ) / upcount[k]
        
        hydrophobic_vol_whole.append((4/3) * 3.14 * ((eff_rad_1_b[k])**3 - (eff_rad_1_b[k] - LC[k])**3))
        
        packing_factor = hydrophobic_vol / (head_area*LC[k])
        
        file_out.writelines(str(k + 1) + '\t' + str(packing_factor) + '\n')
        
    file_out.close()
    
    return hydrophobic_vol_whole
    
   
        
        
        
        


