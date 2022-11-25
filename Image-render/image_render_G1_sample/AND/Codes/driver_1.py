
import sys
import numpy as np
import os

from index import *
from array import array
from measureCOM import *
from read_file import *
from read_file_rem import *
from radius import *
from separation import *
from vesicle_status import *
from status_writer import *
from center_index_finder import *
from mol2_trigger import *
from mol2_trigger_rem import *
from IntCount import *
from MulitpleIntCounts import *
from SelfIntCount import *
from oneDresult import *
from surface import *
from effective_distance import *
from rog import *
from lipid_tail_length import *
from lipid_vol_area import *
from gro_writer import *

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


#############   margin for cutting off amphiphilies that are not a part of the main vesicle ###################    
    margin = float(sys.argv[3])

######### Read input file and convert into the deriable dimensions #############

    array_2D = read_file(filename, NOF, a, size, args[2])
    array_3D = create_array_3D(array_2D, filename, NOF, a, size, args[2])
    array_4D = create_array_4D(array_3D, filename, NOF, a, size, args[2])
    
##### Read the remaining columns that define molecule type #################    
    rem_2D = read_file_rem(filename, NOF, a, size, args[2] + "_rem")
    rem_3D = create_array_3D_rem(rem_2D, filename, NOF, a, size, args[2] + "_rem")
    rem_4D = create_array_4D_rem(rem_3D, filename, NOF, a, size, args[2] + "_rem")


##################################################################################

    COM_1 = FindCOM(array_4D, filename, NOF, a, size, args[2], args[3], args[4])
    [rad, mean, uprad, upcount, lorad, locount, expelled, status] = radiusfinder(COM_1, array_4D, filename, NOF, a, size, args[2], args[3], args[4], margin)
    vesicle_status(rad, uprad, upcount, lorad, locount, expelled, NOF, "DPPC_vesicle_status.out")
##################################################################################

    status_writer(status, NOF, a, size, "DPPC_status_array.out") ## For now, just for book keeping
    center_index_finder(array_4D, status,  NOF, a, size, args[3], args[5])

###############Let us look at the dendron now###########################
    ## Dendron interpreter and Average Neighbor Distance

    [Mol2_4d_array, Mol2_status, mol2_a, mol2_size ] = mol2_reader(sys.argv[2], COM_1, rad, mean, margin)
    
    Mol2_4d_array_rem = mol2_reader_rem(sys.argv[2], COM_1, rad, mean)
#############################################################################

    ## gromacs file writer ###
    
    gro_writer(array_4D, rem_4D, status, a, size, Mol2_4d_array, Mol2_4d_array_rem, Mol2_status, mol2_a, mol2_size, NOF, boxx, boxy, boxz)   
    
    
    

