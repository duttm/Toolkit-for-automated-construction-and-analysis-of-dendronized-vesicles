import numpy
from index_1 import *


def manytooneint(Mol1_array, Mol1_status, Mol2_array, Mol2_status, filename_mol1, filename_mol2, cutoff):

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
    Mol1_iden = args[6]
    print('Groups under consideration for interaction count %s' % (Mol1_iden))
################################################################################
    ints = [int(item) for item in indices(args[3], args[6])]
    i1 = [x - 1 for x in ints]
    ##print(i1)
###############################################################################

    print("Reading Mol2......" + '\n')
    inputfilename = filename_mol2
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
            Mol2_a = int(line.strip())

        if line != "\n":
            line_count += 1

    fp.close()
    print('No. of elements in a single frame is %s' % (Mol2_a))
    Mol2_size = int(args[1])
    print('No. of elements in a single molecule is %s' % (Mol2_size))
    Mol2_NOF = int(line_count / (Mol2_a + 3))
    print('No. of frames in trajectory is %s' % (Mol2_NOF))
    Mol2_iden = args[6]
    print('Groups under consideration for interaction count %s' % (Mol2_iden))

###################################################################################

    ints = [int(item) for item in indices(args[7], args[8])]
    i2 = [x - 1 for x in ints]
    ##print(i2)
#############################################################

    ##Dimension of Mol1_Array

    s1 = int(Mol1_a / Mol1_size)
    s2 = int(Mol2_a / Mol2_size)


    Mol1_rows, Mol1_cols, Mol1_s, Mol1_pages = (Mol1_size, 4, s1, Mol1_NOF)
    Mol2_rows, Mol2_cols, Mol2_s, Mol2_pages = (Mol2_size, 4, s2, Mol2_NOF)

    print("Counting the DPPC head -TA interactions"+'\n')
    print ("{:<30} {:<30} {:<30}".format("Interacting DPPC heads", "Tot Num of DPPC heads", "Fraction of Interacting DPPC heads"))
    m = Mol1_NOF
    counter = [0 for i in range(m)]

    for k in range(Mol2_NOF):
        normalizer = 0
        for l in range(Mol2_s):

            if Mol2_status[k][l] == "outside":

                for yy in range(len(i2)):
                    i = i2[yy]
                    a1 = numpy.array((Mol2_array[i][1][l][k], Mol2_array[i][2][l][k], Mol2_array[i][3][l][k]))
                    normalizer += 1

                    for l1 in range(Mol1_s):
                        if Mol1_status[k][l1] == "outside":
                            for y in range(len(i1)):
                                j = i1[y]
                                a2 = numpy.array((Mol1_array[j][1][l1][k], Mol1_array[j][2][l1][k], Mol1_array[j][3][l1][k]))

                                if (numpy.linalg.norm(a1 - a2)) <= cutoff:
                                    counter[k] = counter[k] + 1
                                    break
                            if (numpy.linalg.norm(a1 - a2)) <= cutoff:
                                break

        print("{:<30} {:<30} {:<30}".format(counter[k], normalizer, counter[k] / normalizer))
        counter[k]=counter[k]/(normalizer)




    return counter


def manytomanyint(Mol1_array, Mol1_status, Mol2_array, Mol2_status, filename_mol1, filename_mol2, cutoff):

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
    Mol1_iden = args[6]
    print('Groups under consideration for interaction count %s' % (Mol1_iden))
################################################################################
    ints = [int(item) for item in indices(args[7], args[8])]
    i1 = [x - 1 for x in ints]
    ##print(i1)
###############################################################################

    print("Reading Mol2......" + '\n')
    inputfilename = filename_mol2
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
            Mol2_a = int(line.strip())

        if line != "\n":
            line_count += 1

    fp.close()
    print('No. of elements in a single frame is %s' % (Mol2_a))
    Mol2_size = int(args[1])
    print('No. of elements in a single molecule is %s' % (Mol2_size))
    Mol2_NOF = int(line_count / (Mol2_a + 3))
    print('No. of frames in trajectory is %s' % (Mol2_NOF))
    Mol2_iden = args[6]
    print('Groups under consideration for interaction count %s' % (Mol2_iden))

###################################################################################

    ints = [int(item) for item in indices(args[7], args[8])]
    i2 = [x - 1 for x in ints]
    ##print(i2)
#############################################################

    ##Dimension of Mol1_Array

    s1 = int(Mol1_a / Mol1_size)
    s2 = int(Mol2_a / Mol2_size)


    Mol1_rows, Mol1_cols, Mol1_s, Mol1_pages = (Mol1_size, 4, s1, Mol1_NOF)
    Mol2_rows, Mol2_cols, Mol2_s, Mol2_pages = (Mol2_size, 4, s2, Mol2_NOF)

    print("Counting the DPPC head - All DEN beads interactions"+'\n')
    print ("{:<30} {:<30} {:<30}".format("Interacting DPPC heads", "Tot Num of DPPC heads", "Fraction of Interacting DPPC heads"))
    m = Mol1_NOF
    counter = [0 for i in range(m)]

    for k in range(Mol2_NOF):
        normalizer = 0
        for l in range(Mol2_s):

            if Mol2_status[k][l] == "outside":

                for yy in range(len(i2)):
                    i = i2[yy]
                    a1 = numpy.array((Mol2_array[i][1][l][k], Mol2_array[i][2][l][k], Mol2_array[i][3][l][k]))
                    normalizer += 1

                    for l1 in range(Mol1_s):
                        if Mol1_status[k][l1] == "outside":
                            for y in range(len(i1)):
                                j = i1[y]
                                a2 = numpy.array((Mol1_array[j][1][l1][k], Mol1_array[j][2][l1][k], Mol1_array[j][3][l1][k]))

                                if (numpy.linalg.norm(a1 - a2)) <= cutoff:
                                    counter[k] = counter[k] + 1
                                    break
                            if (numpy.linalg.norm(a1 - a2)) <= cutoff:
                                break
        print("{:<30} {:<30} {:<30}".format(counter[k], normalizer, counter[k] / normalizer))
        counter[k]=counter[k]/(normalizer)




    return counter
