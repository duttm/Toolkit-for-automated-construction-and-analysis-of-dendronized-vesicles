import numpy
from index_1 import *


def effective_distance(Mol1_array, Mol1_status, NEW_COM, filename_mol1, group_index):

################################################################

    print("Reading Mol1......" + '\n')
    inputfilename = filename_mol1
    f = open(inputfilename, "r")
    lines = f.readlines()
    args = []
    for x in lines:
        args.append(x.split('\t')[1].strip())
    f.close()
    filename = args[0]
    fp = open(filename)
    line_count = 0
    for i, line in enumerate(fp):
        if i == 1:
            Mol1_a = int(line.strip())

        if line != "\n":
            line_count += 1

    fp.close()
    print('No. of elements in a single frame is %s' % (Mol1_a))
    Mol1_size = int(args[1])
    print('No. of elements in a single molecule is %s' % (Mol1_size))
    Mol1_NOF = int(line_count / (Mol1_a + 3))
    print('No. of frames in trajectory is %s' % (Mol1_NOF))
    Mol1_iden = args[group_index]
    print('Groups under consideration for finding effective radius %s' % (Mol1_iden))


##############################################################################

    array = Mol1_array
    s1 = int(Mol1_a / Mol1_size)
    rows, cols, s, pages = (Mol1_size, 4, s1, Mol1_NOF)
    
    ints = [int(item) for item in indices(args[3], args[group_index])]
    i1 = [x - 1 for x in ints]
  
    
    eff_radius = []

    for k in range(pages):
        d = []
        for l in range(s):
           
            if Mol1_status[k][l] == "outside":
                
                for y in range(len(i1)):
                    i = i1[y]
                    a1 = numpy.array((array[i][1][l][k], array[i][2][l][k], array[i][3][l][k]))
                    a2 = numpy.array((NEW_COM[k][0], NEW_COM[k][1], NEW_COM[k][2]))
                    store = numpy.linalg.norm(a1 - a2)
                    d.append(store)
                
        eff_radius.append(sum(d) /len(d))
        
        
    return eff_radius        
                
                

