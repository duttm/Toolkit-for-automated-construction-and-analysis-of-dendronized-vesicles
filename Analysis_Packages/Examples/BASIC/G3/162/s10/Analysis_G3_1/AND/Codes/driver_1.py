
import sys
import numpy as np
import os

from index import *
from array import array
from measureCOM import *
from read_file import *
from radius import *
from separation import *
from vesicle_status import *
from status_writer import *
from center_index_finder import *
from mol2_trigger import *
from IntCount import *
from MulitpleIntCounts import *
from SelfIntCount import *
from oneDresult import *
from surface import *
from effective_distance import *
from rog import *
from lipid_tail_length import *
from lipid_vol_area import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Get input arguments from a text file
    arguments = len(sys.argv) - 1
    inputfilename = sys.argv[1]
    # output argument-wise
    f = open(inputfilename, "r")
    lines = f.readlines()
    args = []
    for x in lines:
        args.append(x.split('\t')[1].strip())
    f.close()

    filename = args[0]

    print('The name of the file is %s' % (filename))

    fp = open(filename)
    line_count = 0
    for i, line in enumerate(fp):
        if i == 1:
            a = int(line.strip())

        if line != "\n":
            line_count += 1

    fp.close()
    box = []
    box = line.split()

    print('No. of elements in a single frame is %s' % (a))
    size = int(args[1])
    print('No. of elements in a single molecule is %s' % (size))


    NOF = int(line_count/(a+3))

    print('No. of frames in trajectory is %s' % (NOF))
    boxx = float(box[0])
    boxy = float(box[1])
    boxz = float(box[2])
    print('Dimensions of box is %s %s %s' % (boxx, boxy, boxz) +'\n')

######### Read input file and convert into the deriable dimensions #############

    array_2D = read_file(filename, NOF, a, size, args[2])
    array_3D = create_array_3D(array_2D, filename, NOF, a, size, args[2])
    array_4D = create_array_4D(array_3D, filename, NOF, a, size, args[2])

##################################################################################

    COM_1 = FindCOM(array_4D, filename, NOF, a, size, args[2], args[3], args[4])
    [rad, mean, uprad, upcount, lorad, locount, expelled, status] = radiusfinder(COM_1, array_4D, filename, NOF, a, size, args[2], args[3], args[4])
    vesicle_status(rad, uprad, upcount, lorad, locount, expelled, NOF, "DPPC_vesicle_status.out")
##################################################################################

    status_writer(status, NOF, a, size, "DPPC_status_array.out") ## For now, just for book keeping
    center_index_finder(array_4D, status,  NOF, a, size, args[3], args[5])

###############Let us look at the dendron now###########################
    ## Dendron interpreter and Average Neighbor Distance

    [Mol2_4d_array, Mol2_status] = mol2_reader(sys.argv[2], COM_1, rad, mean)
#############################################################################

    ##Interaction Counts

    ##Mol1_Mol2_interaction = InteractionC(array_4D, status, Mol2_4d_array, Mol2_status, sys.argv[1], sys.argv[2], 1.2)
    ##Mol2_Mol2_interaction = SelfInteractionC(Mol2_4d_array, Mol2_status, Mol2_4d_array, Mol2_status, sys.argv[2], sys.argv[2], 1.2)
    #
    ##onedresult(Mol1_Mol2_interaction, "TA-PO4", NOF, "TA-PO4.out")
    ##onedresult(Mol2_Mol2_interaction, "TA-TA", NOF, "TA-TA.out")
    #########################################################################################################
    ## Dendron Projected Area
    ##Mol2_Mol1_manytoone = manytooneint(Mol2_4d_array, Mol2_status, array_4D, status, sys.argv[2], sys.argv[1], 1.2)
    ##onedresult(Mol2_Mol1_manytoone, "DPPC (polar heads)-TA", NOF, "DPPC-TA.out")
    ##surfacecalc(Mol2_Mol1_manytoone, uprad, NOF, "Dendron_Projected_area_TAbeads.out")

    ##Mol2_Mol1_manytomany = manytomanyint(Mol2_4d_array, Mol2_status, array_4D, status, sys.argv[2], sys.argv[1], 1.2)
    ##onedresult(Mol2_Mol1_manytomany, "DPPC (polar heads)-DEN (All head beads)", NOF, "DPPC-DEN.out")
    ##surfacecalc(Mol2_Mol1_manytomany, uprad, NOF, "Dendron_Projected_area_allDENbeads.out")
    
    
    #######################################################################################################
    ## A new COM is required after the expelled amphiphiles were removed ##############
    NEW_COM = recomputeCOM(array_4D, status, filename, NOF, a, size, args[2], args[3], args[4])
    ############################################################################################
    
    #### What is the effective radius considering PO4 beads of Lipids? #########################
    ##eff_rad_1 = effective_distance(array_4D, status, NEW_COM, sys.argv[1], 6 )
    ##onedresult(eff_rad_1, "Rad[PO4-COM]", NOF, "effective_rad_PO4.out")
    ##########################################################################################
    
    #### What is the effective radius considering NC3 beads of Lipids? #########################
    eff_rad_1_a = effective_distance(array_4D, status, NEW_COM, sys.argv[1], 11 )
    onedresult(eff_rad_1_a, "Rad[NC3-COM]", NOF, "effective_rad_NC3.out")
    ##########################################################################################
    
    #### What is the effective radius considering GL1 beads of Lipids? #########################
    eff_rad_1_b = effective_distance(array_4D, status, NEW_COM, sys.argv[1], 12 )
    onedresult(eff_rad_1_b, "Rad[GL1-COM]", NOF, "effective_rad_GL1.out")
    ##########################################################################################
    

    #### What is the effective radius considering Terminal Amines of Dendrons? #########################
    
    ##eff_rad_2 = effective_distance(Mol2_4d_array, Mol2_status, NEW_COM, sys.argv[2], 6) 
    ##onedresult(eff_rad_2, "Rad[Qd-COM]", NOF, "effective_rad_Qd.out")
    
#### What is the effective radius considering Amindes of Dendrons? #########################
    
    ##eff_rad_3 = effective_distance(Mol2_4d_array, Mol2_status, NEW_COM, sys.argv[2], 9)
    ##onedresult(eff_rad_3, "Rad[P3-COM]", NOF, "effective_rad_P3.out")
    
#### What is the effective radius considering Tertiary Amines of Dendrons? #########################
    
    ##eff_rad_4 = effective_distance(Mol2_4d_array, Mol2_status, NEW_COM, sys.argv[2], 10)
    ##onedresult(eff_rad_4, "Rad[N0-COM]", NOF, "effective_rad_N0.out")
    
###### What is the ROG on individual dendrons on the outer surface of the vesicle (due to TA)#####################

    ##eff_rog_TA = rog(Mol2_4d_array, Mol2_status, sys.argv[2], 6)
    ##onedresult(eff_rog_TA, "ROG of Dendrons [TA]", NOF, "ROG_DENS_TA.out")     
    ########################################################################################
    ###### What is the ROG on individual dendrons on the outer surface of the vesicle (due to P3)#####################

    ##eff_rog_P3 = rog(Mol2_4d_array, Mol2_status, sys.argv[2], 9)
    ##onedresult(eff_rog_P3, "ROG of Dendrons [P3]", NOF, "ROG_DENS_P3.out")     
    ########################################################################################
    
    ###### What is the ROG on individual dendrons on the outer surface of the vesicle (due to N0)#####################

    ##eff_rog_N0 = rog(Mol2_4d_array, Mol2_status, sys.argv[2], 10)
    ##onedresult(eff_rog_N0, "ROG of Dendrons [N0]", NOF, "ROG_DENS_N0.out")     
    ########################################################################################
    
    ###### What is the ROG on individual dendrons on the outer surface of the vesicle (due to N0)#####################

    ##eff_rog_ALL = rog_all(Mol2_4d_array, Mol2_status, sys.argv[2])
    ##onedresult(eff_rog_ALL, "ROG of Dendrons [ALL BEADS]", NOF, "ROG_DENS_ALL.out")     
    ########################################################################################
    
    ###### What is the thickness of the dendron layer? ####################
    ##onedresult_1(eff_rad_2, eff_rad_1,  "Thickness of Dendron Layer", NOF, "Den_layer_thickness.out")     
    ########################################################################################
###### What is distribution of all terminal amines (reference is COM of dendron ?#####################

    ##TA_dist = rog_dist(Mol2_4d_array, Mol2_status, sys.argv[2], 6)
    ##onedresult_2(TA_dist, "DIST TA from COM [nm]", NOF, "Dist_TAs_from_COM.out")     
    ########################################################################################
    
    
###### What is distribution of all terminal amines (reference is grafting point of dendron ?#####################

    ##TA_dist_1 = rog_dist_1(Mol2_4d_array, Mol2_status, sys.argv[2], 6)
    ##onedresult_2(TA_dist_1, "DIST TA from graftin pt [nm]", NOF, "Dist_TAs_from_grafting_point.out")     
    ########################################################################################

###### What is distribution of all amides (reference is COM ?#####################

    ##P3_dist = rog_dist(Mol2_4d_array, Mol2_status, sys.argv[2], 9)
    ##onedresult_2(P3_dist, "DIST P3 from COM [nm]", NOF, "Dist_P3s_from_COM.out")     
    ########################################################################################
    
    
###### What is distribution of all amides (reference is grafting point ?#####################

    ##P3_dist_1 = rog_dist_1(Mol2_4d_array, Mol2_status, sys.argv[2], 9)
    ##onedresult_2(P3_dist_1, "DIST P3 from grafting point [nm]", NOF, "Dist_P3s_from_grafting_point.out")     
    ########################################################################################

###### What is distribution of all tertiary amines (reference is COM ?#####################

    ##P3_dist = rog_dist(Mol2_4d_array, Mol2_status, sys.argv[2], 10)
    ##onedresult_2(P3_dist, "DIST N0 from COM [nm]", NOF, "Dist_N0s_from_COM.out")     
    ########################################################################################
    
    
###### What is distribution of all tertiary amines (reference is grafting point ?#####################

    ##P3_dist_1 = rog_dist_1(Mol2_4d_array, Mol2_status, sys.argv[2], 10)
    ##onedresult_2(P3_dist_1, "DIST N0 from grafting point [nm]", NOF, "Dist_N0s_from_grafting_point.out")     
    ########################################################################################

##### Find the length of the Lipid Tails ##############    
    
    
    LC = LCfinder(NEW_COM, array_4D, status, NOF, a, size, moleculefile = args[3], index_1 = args[9], index_2 = args[10])
    printLC(LC, NOF, "LC.out")
    
#### Find area occupied by the lipid had beads ###############################
    
    hydrophobic_vol_whole = pack_factor(eff_rad_1_a , upcount, LC, eff_rad_1_b, NOF, "packing_factor", "packing_factor.out")
    onedresult(hydrophobic_vol_whole, "Outer_hydrophobic_vol", NOF, "hydrophobic_vol.out")    
    
    
    

