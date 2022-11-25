
import sys
import numpy as np
import os

from array import array

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def read_file(filename, NOF, a, size):


    y = 0
    f = open(filename, "r")
    lines = f.readlines()

    result = []
    for x in lines:
        result.append(x)
        y = y + 1

    f.close()

    print(y)
    counter = 0
    refine = []
    x = 0

    while x <= (a + 3) * (NOF + 1):
        if x == 0 or x == 1:  # skip first 2 lines
            counter = counter + 1
            x = x + 1
            # print("x is %s and counter in %s in stage 1" % (x, counter))

        elif 2 <= counter <= a + 1:
            refine.append(result[x])
            x = x + 1
            counter = counter + 1
            # print("x is %s and counter in %s in stage 2" % (x, counter))

        elif counter == a + 2:
            counter = 2
            x = x + 3
            if x > y:
                break
            # print("x is %s and counter in %s in stage 3" % (x, counter))

        else:
            print(0)

    file_out = open("array.txt", "w")

    # admit values into a large 2D array

    rows, cols = (a * NOF, 4)
    array = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(a * NOF):
        # print(i)
        t = refine[i][0:8]
        id = refine[i][15:20]  # Column values may vary on the basis of gromacs version
        x = refine[i][21:28]
        y = refine[i][29:36]
        z = refine[i][37:44]
        array[i][0] = id
        array[i][1] = x
        array[i][2] = y
        array[i][3] = z



    for i in range(rows):
        file_out.writelines(str(array[i]) + '\n')
        # view array.txt to check
    file_out.close()

    return array




def create_array_3D(array_2D, filename, NOF, a , size):


    array = array_2D
    # 2d big to 3D small conversion

    rows, cols, pages = (a, 4, NOF)
    array3d = [[[0 for k in range(pages)] for i in range(cols)] for j in range(rows)]

    h = 0

    for k in range(pages):
        for i in range(rows):
            array3d[i][0][k] = float(array[h][0])
            array3d[i][1][k] = float(array[h][1])
            array3d[i][2][k] = float(array[h][2])
            array3d[i][3][k] = float(array[h][3])
            h = h + 1

    file_out1 = open("array3d.txt", "w")

    # view array3d.txt to check

    for k in range(pages):
        for i in range(rows):
            file_out1.writelines(
                str(array3d[i][0][k]) + ',' + str(array3d[i][1][k]) + ',' + str(
                    array3d[i][2][k]) + ',' + str(array3d[i][3][k]) + ',' + str(k) + '\n')

    file_out1.close()

    return array3d

    # Now lets do 4D

def create_array_4D(array_3D, filename, NOF, a, size):

    array3d = array_3D
    s1 = int(a / size)

    rows, cols, s, pages = (size, 4, s1, NOF)
    array4d = [[[[0 for k in range(pages)] for l in range(s)] for i in range(cols)] for j in range(rows)]

    for k in range(pages):
        h = 0
        for l in range(s):
            for i in range(rows):
                array4d[i][0][l][k] = array3d[h][0][k]
                array4d[i][1][l][k] = array3d[h][1][k]
                array4d[i][2][l][k] = array3d[h][2][k]
                array4d[i][3][l][k] = array3d[h][3][k]
                h = h + 1

    file_out4d = open("array4d.txt", "w")

    # view array4d.txt to check

    for k in range(pages):
        for l in range(s):
            for i in range(rows):
                file_out4d.writelines(str(array4d[i][0][l][k]) + ',' + str(array4d[i][1][l][k]) + ',' + str(
                    array4d[i][2][l][k]) + ',' + str(array4d[i][3][l][k]) + ' ' + str(k) + '\n')

            file_out4d.writelines('\n')

    file_out4d.close()

    return array4d


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

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
    print('Dimensions of box is %s %s %s' % (boxx, boxy, boxz))


    # x1 = float(sys.argv[8])
    # y1 = float(sys.argv[10])
    # z1 = float(sys.argv[12])
    #
    # x2 = float(sys.argv[9])
    # y2 = float(sys.argv[11])
    # z2 = float(sys.argv[13])

    # print('Extract coordinates within this zone is x= %s and %s y= %s and %s z= %s and %s' % (x1, x2, y1, y2, z1, z2))
    #####################################################################

    # array_2D = read_file(filename, NOF, a, size)
    # array_3D = create_array_3D(array_2D, filename, NOF, a, size)
    # array_4D = create_array_4D(array_3D, filename, NOF, a, size)

    # [modify_4D, new_size] = modify(array_4D, filename, NOF, a, size, x1, x2, y1, y2, z1, z2)

    #write_gro_file(modify_4D, filename, NOF, new_size, size, boxx, boxy, boxz)









