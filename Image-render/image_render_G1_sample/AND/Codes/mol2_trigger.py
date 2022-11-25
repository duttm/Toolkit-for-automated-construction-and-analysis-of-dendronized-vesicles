import sys
import numpy as np
import os

from read_file import *
from radius_mol2 import *
from vesicle_status import *
from AvgND import *
from status_writer import *

def mol2_reader(filename, COM, rad, mean, margin):

    print("Reading Dendrons......"+'\n')
    inputfilename = filename
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
    print('Dimensions of box is %s %s %s' % (boxx, boxy, boxz))
    
######### Read input file and convert into the deriable dimensions #############

    array_2D = read_file(filename, NOF, a, size, args[2])
    array_3D = create_array_3D(array_2D, filename, NOF, a, size, args[2])
    array_4D = create_array_4D(array_3D, filename, NOF, a, size, args[2])

##################################################################################
    ## Taking the DPPC_COM as the COM for dendrons
    
    [uprad, upcount, lorad, locount, expelled, status] = radius_mol2(rad, mean, COM, array_4D, filename, NOF, a, size, args[2], args[3], args[4], margin)
    vesicle_status(rad, uprad, upcount, lorad, locount, expelled, NOF, "DEN_vesicle_status.out")
    status_writer(status, NOF, a, size, "DEN_status_array.out")
    
    ## Note that mean radius is calculated with DPPC beads only.
#############################################################################
    ## Find the Average Neighbor Distance

    AND = AvgND(array_4D, status, NOF, a, size, args[2], args[3], args[4])

    printAND(AND, NOF, "AND_results.out")

    return array_4D, status, a, size












