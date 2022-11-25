import numpy
from index import *


def AvgND(array_4D, status, NOF, a, size, outfile, moleculefile, indexing):
    array = array_4D
    s1 = int(a / size)
    rows, cols, s, pages = (size, 4, s1, NOF)



    i = int(index(moleculefile, indexing)) - 1

    s2 = []

    for k in range(NOF):
        s1 = []
        for l in range(s - 1):
            d = []

            if status[k][l] == "outside":
                a1 = numpy.array((array[i][1][l][k], array[i][2][l][k], array[i][3][l][k]))
                for c in range(l+1,s):
                    if status[k][c] == "outside":
                        a2 = numpy.array((array[i][1][c][k], array[i][2][c][k], array[i][3][c][k]))
                        store = numpy.linalg.norm(a1 - a2)
                        ##print(store, l, c)
                        d.append(store)
                if d:
                    s1.append(min(d))
        s2.append(sum(s1)/len(s1))

    return s2

def printAND(AND, NOF, output_textfile):


    file_out = open(output_textfile, "w")

    file_out.writelines("Frame" + '\t' + "AND" + '\n')
    for k in range(NOF):
        file_out.writelines(str(k + 1) + '\t' + str(AND[k]) + '\n')
    file_out.close()



