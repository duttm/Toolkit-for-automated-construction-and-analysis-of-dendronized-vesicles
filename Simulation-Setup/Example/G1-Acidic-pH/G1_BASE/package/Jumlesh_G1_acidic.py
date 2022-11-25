import sys
import math
import numpy as np
import matplotlib.pyplot as plt

import time


# execution style : python Jumlesh.py
# <1. name of lipid file>
# <2. Number of Frames >
# <3. Number of rows in one frame >
# <4. Number of beads/atoms in one molecule>
# <5. Distance of grafting point from corner >
# <6. Grid>
# <7. Name of dendron up file >
# <8. Number of frames >
# <9. Number of rows in 1 frame >
# <10. Number of beads/atoms in one molecule >
# <11. Name of dendron down file >
# <12. Number of frames >
# <13. Number of rows in 1 frame >
# <14. Number of beads/atoms in one molecule >
# <15. Skip value >

# sample run : python3 Jumlesh.py dppc_3002.gro 1 36468 12 1 4 den_up_G2.gro 1 31 31 den_down_G2.gro 1 31 31 1


# How different concentrations of dendrons/PEGs can be generated ? -> Use different combinations of grid and skip.

def main():
    # count the arguments
    arguments = len(sys.argv) - 1

    # output argument-wise

    ###### command line section ####################

    filename = sys.argv[1]
    print('filename is %s' % (filename))
    NOF = int(sys.argv[2])
    print('NOF is %s' % (NOF))
    a = int(sys.argv[3])
    print('No. of elements in a single frame is %s' % (a))
    size = int(sys.argv[4])
    skip=float(sys.argv[15])
    relax_gap=float(sys.argv[16])

    #####################################################################

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

    # Now lets do 4D

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

    ## lets use Lipid Polar head ( id =1 ) to get a COM for the bilayer system

    cen_x = 0
    cen_y = 0
    cen_z = 0

    players = 0

    for k in range(pages):
        for l in range(s):
            cen_x = cen_x + array4d[0][1][l][k]
            cen_y = cen_y + array4d[0][2][l][k]
            cen_z = cen_z + array4d[0][3][l][k]
            players = players + 1

    cen_x = cen_x / players
    cen_y = cen_y / players
    cen_z = cen_z / players

    print(cen_x, cen_y, cen_z)

    ## Lets distinguish between upper and lower monolayer lipids : assign lipid ids to 1d array

    # from array import array
    # bond_dist_filter_1 = array('d')  # 'd' denotes an array of type double
    #
    # h_b_1 = 0
    # for k in range(h_b):
    #     if bond_dist[k] <= thres:
    #         bond_dist_filter_1.append(bond_dist[k])
    #         h_b_1 = h_b_1 + 1

    from array import array

    lower_mono_count = array('d')
    upper_mono_count = array('d')

    l_count = 0
    u_count = 0

    for k in range(pages):
        for l in range(s):
            if (array4d[0][3][l][k] > cen_z):
                upper_mono_count.append(l)
                u_count = u_count + 1

            else:

                lower_mono_count.append(l)
                l_count = l_count + 1

    file_out_lower = open("lower_mono.txt", "w")

    # view lower_mono.txt to check

    for k in range(l_count):
        file_out_lower.writelines(str(lower_mono_count[k]) + '\n')

    file_out_lower.close()

    file_out_upper = open("upper_mono.txt", "w")

    # view upper_mono.txt to check

    for k in range(u_count):
        file_out_upper.writelines(str(upper_mono_count[k]) + '\n')

    file_out_upper.close()

    ## Lets find minx, min y -----

    minx = array4d[0][1][0][0]
    maxx = array4d[0][1][s - 1][0]

    miny = array4d[0][2][0][0]
    maxy = array4d[0][2][s - 1][0]

    for k in range(pages):
        for l in range(s):

            if array4d[0][1][l][k] < minx:

                minx = array4d[0][1][l][k]

            elif array4d[0][1][l][k] > maxx:

                maxx = array4d[0][1][l][k]

            if array4d[0][2][l][k] < miny:

                miny = array4d[0][2][l][k]

            elif array4d[0][2][l][k] > maxy:

                maxy = array4d[0][2][l][k]

    print(minx, maxx)
    print(miny, maxy)

    edge = int(sys.argv[5])

    minx = minx + edge
    miny = miny + edge
    maxx = maxx - edge
    maxy = maxy - edge

    grid = int(sys.argv[6])

    x_gap = (maxx - minx) / grid
    y_gap = (maxy - miny) / grid

    print(x_gap, y_gap)

    x_match = 0
    y_match = 0
    store_up_id = array('d')
    store_low_id = array('d')
    up_count = 0
    low_count = 0
    cut = 0.6
    not_unique = 0
    ## Lets find the grafting points



    for i in range(int ((grid + 1)/skip)):
        for j in range(int ((grid + 1)/skip)):

            x_match = minx + x_gap * i
            y_match = miny + y_gap * j

            for k in range(pages):
                for l in range(u_count):

                    if (abs(array4d[0][1][l][k] - x_match) < cut) and (abs(array4d[0][2][l][k] - y_match) < cut):

                        not_unique = 0
                        for u in range(up_count):
                            if store_up_id[u] == l:
                                not_unique = 1
                        if not_unique == 0:
                            store_up_id.append(l)
                            up_count = up_count + 1
                            break

            for k in range(pages):
                for l in range(u_count + 1, s):

                    if (abs(array4d[0][1][l][k] - x_match) < cut) and (abs(array4d[0][2][l][k] - y_match) < cut):

                        not_unique = 0
                        for u in range(low_count):
                            if store_low_id[u] == l:
                                not_unique = 1
                        if not_unique == 0:
                            store_low_id.append(l)
                            low_count = low_count + 1
                            break

    file_store_up_id = open("store_up_id.txt", "w")

    # view upper_mono.txt to check

    for k in range(up_count):
        file_store_up_id.writelines(str(store_up_id[k]) + '\n')

    file_store_up_id.close()

    file_store_low_id = open("store_low_id.txt", "w")

    # view upper_mono.txt to check

    for k in range(low_count):
        file_store_low_id.writelines(str(store_low_id[k]) + '\n')

    file_store_low_id.close()

    ## Writing to gro format

    Col4 = ['NC3', 'PO4', 'GL1', 'GL2', 'C1A', 'C2A', 'C3A', 'C4A', 'C1B', 'C2B', 'C3B', 'C4B']
    Col5 = ['DPPC']

    print(Col4[5])

    D1 = array('i')
    D2 = []
    D3 = []
    D4 = array('i')
    D5 = array('d')
    D6 = array('d')
    D7 = array('d')

    l1 = 1
    m = 1

    for k in range(pages):
        for l in range(up_count):

            for i in range(rows):
                temp_s = int(store_up_id[l])
                D1.append(l1)
                D2.append(Col5[0])
                D3.append(Col4[i])
                D4.append(m)
                D5.append(array4d[i][1][temp_s][k])
                D6.append(array4d[i][2][temp_s][k])
                D7.append(array4d[i][3][temp_s][k])

                m = m + 1

            l1 = l1 + 1

        for l in range(low_count):

            for i in range(rows):
                temp_s = int(store_low_id[l])
                D1.append(l1)
                D2.append(Col5[0])
                D3.append(Col4[i])
                D4.append(m)
                D5.append(array4d[i][1][temp_s][k])
                D6.append(array4d[i][2][temp_s][k])
                D7.append(array4d[i][3][temp_s][k])

                m = m + 1

            l1 = l1 + 1

    file_write_DPPC = open("write_DPPC.gro", "w")

    # view upper_mono.txt to check

    file_write_DPPC.writelines('we are making a grid' + '\n')
    file_write_DPPC.write(str(m - 2) + '\n')
    for k in range(m - 2):
        file_write_DPPC.writelines(
            '{:>5}'.format(str(D1[k])) + '{:>5}'.format(str(D2[k])) + '{:>5}'.format(str(D3[k])) + '{:>5}'.format(
                str(D4[k])) + '{:8.3f}'.format(D5[k]) + '{:8.3f}'.format(D6[k]) + '{:8.3f}'.format(D7[k]) + '\n')

    file_write_DPPC.writelines('{:8.3f}'.format(maxx) + '{:8.3f}'.format(maxy) + '{:8.3f}'.format(15))
    file_write_DPPC.close()

    ####### Lets read Dendron file ##############################


###################UP#############################################
    ###### command line section ####################

    filename = sys.argv[7]
    print('filename is %s' % (filename))
    NOF = int(sys.argv[8])
    print('NOF is %s' % (NOF))
    a = int(sys.argv[9])
    print('No. of elements in a single frame is %s' % (a))
    size = int(sys.argv[10])
    # thres=float(sys.argv[5])

    #####################################################################

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

    # 2d big to 3D small conversion

    rows, cols, pages = (a, 4, NOF)
    den = [[[0 for k in range(pages)] for i in range(cols)] for j in range(rows)]

    h = 0

    for k in range(pages):
        for i in range(rows):
            den[i][0][k] = float(array[h][0])
            den[i][1][k] = float(array[h][1])
            den[i][2][k] = float(array[h][2])
            den[i][3][k] = float(array[h][3])
            h = h + 1

    file_out1 = open("den.txt", "w")

    # view array3d.txt to check

    for k in range(pages):
        for i in range(rows):
            file_out1.writelines(
                str(den[i][0][k]) + ',' + str(den[i][1][k]) + ',' + str(
                    den[i][2][k]) + ',' + str(den[i][3][k]) + ',' + str(k) + '\n')

    file_out1.close()
##########################################################################################

    ################################DOWN##############################################

    ###### command line section ####################

    filename = sys.argv[11]
    print('filename is %s' % (filename))
    NOF = int(sys.argv[12])
    print('NOF is %s' % (NOF))
    a = int(sys.argv[13])
    print('No. of elements in a single frame is %s' % (a))
    size = int(sys.argv[14])
    # thres=float(sys.argv[5])

    #####################################################################

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

    # 2d big to 3D small conversion

    rows, cols, pages = (a, 4, NOF)
    den_down = [[[0 for k in range(pages)] for i in range(cols)] for j in range(rows)]

    h = 0

    for k in range(pages):
        for i in range(rows):
            den_down[i][0][k] = float(array[h][0])
            den_down[i][1][k] = float(array[h][1])
            den_down[i][2][k] = float(array[h][2])
            den_down[i][3][k] = float(array[h][3])
            h = h + 1

    file_out1 = open("den_down.txt", "w")

    # view array3d.txt to check

    for k in range(pages):
        for i in range(rows):
            file_out1.writelines(
                str(den_down[i][0][k]) + ',' + str(den_down[i][1][k]) + ',' + str(
                    den_down[i][2][k]) + ',' + str(den_down[i][3][k]) + ',' + str(k) + '\n')

    file_out1.close()

    ############################################################################################
    ######## translation of coordinates

    new_den = [[[0 for k in range(pages)] for i in range(cols)] for j in range((rows + 8) * (up_count+low_count)) ]

    h = 0
    for k in range(pages):

        for l in range(up_count):

            for i in range(rows):
                temp_s = int(store_up_id[l])
                new_den[h][1][k] = den[i][1][k] - (den[0][1][k] - array4d[3][1][temp_s][k])
                new_den[h][2][k] = den[i][2][k] - (den[0][2][k] - array4d[3][2][temp_s][k])
                new_den[h][3][k] = den[i][3][k] - (den[0][3][k] - array4d[3][3][temp_s][k]) + relax_gap
                h = h + 1

            for j in range(4, 12):
                temp_s = int(store_up_id[l])
                new_den[h][1][k] = array4d[j][1][temp_s][k]
                new_den[h][2][k] = array4d[j][2][temp_s][k]
                new_den[h][3][k] = array4d[j][3][temp_s][k]
                h = h + 1


    for k in range(pages):

        for l in range(low_count):

            for i in range(rows):
                temp_s = int(store_low_id[l])
                new_den[h][1][k] = den_down[i][1][k] - (den_down[0][1][k] - array4d[3][1][temp_s][k])
                new_den[h][2][k] = den_down[i][2][k] - (den_down[0][2][k] - array4d[3][2][temp_s][k])
                new_den[h][3][k] = den_down[i][3][k] - (den_down[0][3][k] - array4d[3][3][temp_s][k]) - relax_gap
                h = h + 1

            for j in range(4, 12):
                temp_s = int(store_low_id[l])
                new_den[h][1][k] = array4d[j][1][temp_s][k]
                new_den[h][2][k] = array4d[j][2][temp_s][k]
                new_den[h][3][k] = array4d[j][3][temp_s][k]
                h = h + 1




    from array import array

    C1 = array('i')
    C2 = []
    C3 = []
    C4 = array('i')
    C5 = array('d')
    C6 = array('d')
    C7 = array('d')



    h = 0
    l1 = 1

    Col_DEN = []

    N_counter = 1
    N1_counter = 0
    N_check = 0
    Q_counter = 1
    Q1_counter = 0
    Q_check = 0

    int_count = 0


######legacy for neutral dendrons#############################################
    #for i in range(rows):

        #if i < (rows - 30):  ## Need to change the X in " rows - X " for other dendrons !!

         #   Col_DEN.append('N' + str(N_counter))
          #  N_counter = N_counter + 1

       # if (rows - 30) <= i:  ## Need to change the X in " rows - X " for other dendrons !!

        #    if Q_check == 0:
         #       Col_DEN.append('Q' + str(Q_counter))
          #      Q_counter = Q_counter + 1
           #     Q1_counter = Q1_counter + 1

            #    if Q1_counter % 2 == 0:
             #       Q_check = 1


           # else:
            #    Col_DEN.append('N' + str(N_counter))
             #   N_counter = N_counter + 1
              #  N1_counter = N1_counter + 1

               # if N1_counter % 2 == 0:
                #    Q_check = 0
                    
                    
#######################################################################################                    

    for i in range(rows):

        if i == 0 or i == 1 or i == 4 or i == 6:  ## Need to change the X in " rows - X " for other dendrons !!

            Col_DEN.append('Q' + str(Q_counter))
            Q_counter = Q_counter + 1
            
        #elif i == 1:  ## Need to change the X in " rows - X " for other dendrons !!

            #Col_DEN.append('N' + str(N_counter))
            #N_counter = N_counter + 1      
                
                
        elif i == 2 or i == 3 or i == 5:  ## Need to change the X in " rows - X " for other dendrons !!

            Col_DEN.append('N' + str(N_counter))
            N_counter = N_counter + 1 
            
            
        
                

        else:  ## Need to change the X in " rows - X " for other dendrons !!

            if N_check == 0:
                Col_DEN.append('N' + str(N_counter))
                N_counter = N_counter + 1
                N1_counter = N1_counter + 1

                if N1_counter % 2 == 0:
                    N_check = 1


            else:
                Col_DEN.append('Q' + str(Q_counter))
                Q_counter = Q_counter + 1
                Q1_counter = Q1_counter + 1

                if Q1_counter % 2 == 0:
                    N_check = 0

    Col_DEN.append('C1')
    Col_DEN.append('C2')
    Col_DEN.append('C3')
    Col_DEN.append('C4')
    Col_DEN.append('C1')
    Col_DEN.append('C2')
    Col_DEN.append('C3')
    Col_DEN.append('C4')




    m = 1

    h = 0

    for k in range(pages):

       for l1 in range(up_count+low_count):
          for i in range((rows + 8)):
                C1.append(l1+1)
                C2.append('DEN')
                C3.append(Col_DEN[i])
                C4.append(m)
                C5.append(new_den[h][1][k])
                C6.append(new_den[h][2][k])
                C7.append(new_den[h][3][k])

                h = h + 1

                m = m + 1








    file_write_DEN = open("write_DEN_new.gro", "w")

    # view upper_mono.txt to check

    file_write_DEN.writelines('we are making a grid' + '\n')
    file_write_DEN.write(str((a+8)*(up_count+low_count)) + '\n')
    for k in range((a+8)*(up_count+low_count)):
        file_write_DEN.writelines(
            '{:>5}'.format(str(C1[k])) + '{:>5}'.format(str(C2[k])) + '{:>5}'.format(str(C3[k])) + '{:>5}'.format(
                str(C4[k])) + '{:8.3f}'.format(C5[k]) + '{:8.3f}'.format(C6[k]) + '{:8.3f}'.format(C7[k]) + '\n')

    file_write_DEN.writelines('{:8.3f}'.format(maxx) + '{:8.3f}'.format(maxy) + '{:8.3f}'.format(15))
    file_write_DEN.close()

    file_write_comb = open("combined.gro", "w")

    # view upper_mono.txt to check

    file_write_comb.writelines('we are making a grid' + '\n')
    file_write_comb.write(str((a + 8) * (up_count + low_count)  + (3039 - (up_count + low_count)) * 12   ) + '\n')
    for k in range((a + 8) * (up_count + low_count)  ):
        file_write_comb.writelines(
            '{:>5}'.format(str(C1[k])) + '{:>5}'.format(str(C2[k])) + '{:>5}'.format(str(C3[k])) + '{:>5}'.format(
                str(C4[k])) + '{:8.3f}'.format(C5[k]) + '{:8.3f}'.format(C6[k]) + '{:8.3f}'.format(C7[k]) + '\n')

    # file_write_DEN.writelines('{:8.3f}'.format(maxx) + '{:8.3f}'.format(maxy) + '{:8.3f}'.format(15))
    # file_write_DEN.close()



##########################################################################################################

##### Combined Writer Program ##########################################

    ###### REPEAT LIPID DETAILS ####################

    filename = sys.argv[1]
    print('filename is %s' % (filename))
    NOF = int(sys.argv[2])
    print('NOF is %s' % (NOF))
    a = int(sys.argv[3])
    print('No. of elements in a single frame is %s' % (a))
    size = int(sys.argv[4])
    # thres=float(sys.argv[5])

    #####################################################################

    Col4 = ['NC3', 'PO4', 'GL1', 'GL2', 'C1A', 'C2A', 'C3A', 'C4A', 'C1B', 'C2B', 'C3B', 'C4B']
    Col5 = ['DPPC']



    print(Col4[5])

    NOL = int(a/size)

    E1 = array('i')
    E2 = []
    E3 = []
    E4 = array('i')
    E5 = array('d')
    E6 = array('d')
    E7 = array('d')

    m1 = 1

    l1 = l1 + 2

    for k in range(pages):


            for i in range(u_count):

                up_check = 0
                for j in range(up_count):

                  temp_s = int(store_up_id[j])

                  if i == temp_s:

                      up_check = 1

                if up_check != 1:
                  for c in range(12):

                        E1.append(l1)
                        E2.append(Col5[0])
                        E3.append(Col4[c])

                        E4.append(m)
                        E5.append(array4d[c][1][i][k])
                        E6.append(array4d[c][2][i][k])
                        E7.append(array4d[c][3][i][k])

                        m = m + 1
                        m1 = m1 + 1

                  l1 = l1 + 1

            for i in range(u_count, (u_count+ l_count) ):

                low_check = 0

                for j in range(low_count):

                    temp_s = int(store_low_id[j])

                    if i == temp_s:

                        low_check = 1

                if low_check != 1:
                   for c in range(12):

                            E1.append(l1)
                            E2.append(Col5[0])
                            E3.append(Col4[c])
                            E4.append(m)
                            E5.append(array4d[c][1][i][k])
                            E6.append(array4d[c][2][i][k])
                            E7.append(array4d[c][3][i][k])

                            m = m + 1
                            m1 = m1 + 1

                   l1 = l1 + 1




    for k in range(m1 - 1):
        file_write_comb.writelines(
            '{:>5}'.format(str(E1[k])) + '{:>5}'.format(str(E2[k])) + '{:>5}'.format(str(E3[k])) + '{:>5}'.format(
                str(E4[k])) + '{:8.3f}'.format(E5[k]) + '{:8.3f}'.format(E6[k]) + '{:8.3f}'.format(E7[k]) + '\n')

    file_write_comb.writelines('{:8.3f}'.format(maxx) + '{:8.3f}'.format(maxy) + '{:8.3f}'.format(15))
    file_write_comb.close()


### Section for later use ######


class Bead(object):
    def __init__(self, id, x_dim, y_dim, z_dim):
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.z_dim = z_dim


######################################################################

if __name__ == "__main__":
    main()
