import sys
import numpy as np
import os

from read_file import *
from read_file_rem import *
from radius_mol2 import *
from vesicle_status import *
from AvgND import *
from status_writer import *

def mol2_reader_rem(filename, COM, rad, mean):

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

    rem_2D = read_file_rem(filename, NOF, a, size, args[2] + "rem")
    rem_3D = create_array_3D_rem(rem_2D, filename, NOF, a, size, args[2] + "rem")
    rem_4D = create_array_4D_rem(rem_3D, filename, NOF, a, size, args[2] + "rem")

##################################################################################

    return rem_4D












