import numpy

from index import *

def LCfinder(NEW_COM, array_4D, status, NOF, a, size, moleculefile, index_1, index_2):


    array = array_4D
    s1 = int(a / size)
    rows, cols, s, pages = (size, 4, s1, NOF)

    s2 = []
    
    start = int(index(moleculefile, index_1)) - 1
    end = int(index(moleculefile, index_2)) - 1
    for k in range(NOF):
        d1 = []
        for l in range(s):
            if status[k][l] == "outside":
                d = []
                for i in range(start,end):
                    
                    a1 = numpy.array((array[i][1][l][k], array[i][2][l][k], array[i][3][l][k]))
                    a2 = numpy.array((NEW_COM[k][0], NEW_COM[k][1], NEW_COM[k][2]))
                    store = numpy.linalg.norm(a1 - a2)
                    d.append(store)
                d1.append(max(d)-min(d))
        s2.append(sum(d1)/len(d1))

    return s2

def printLC(AND, NOF, output_textfile):


    file_out = open(output_textfile, "w")

    file_out.writelines("Frame" + '\t' + "LC" + '\n')
    for k in range(NOF):
        file_out.writelines(str(k + 1) + '\t' + str(AND[k]) + '\n')
    file_out.close()



