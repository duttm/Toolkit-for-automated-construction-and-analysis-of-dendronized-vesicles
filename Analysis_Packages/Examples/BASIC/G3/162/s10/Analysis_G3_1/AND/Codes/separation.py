import numpy
from index import *


def separater(rad, status, array_4D, filename, NOF, a, size, moleculefile, indexing):

    array = array_4D
    s1 = int(a / size)
    rows, cols, s, pages = (size, 4, s1, NOF)



    for k in range(pages):

        for l in range(s):

            i = int(index(moleculefile, indexing))-1

            a = numpy.array((COM[k][0], COM[k][1], COM[k][2]))
            b = numpy.array((array[i][1][l][k], array[i][2][l][k], array[i][3][l][k]))


            if numpy.linalg.norm(a - b) > rad[k] and numpy.linalg.norm(a - b) < 2*rad[k] :
                upcount[k] = upcount[k] + 1

            elif numpy.linalg.norm(a - b) < rad[k]:
                locount[k] = locount[k] + 1






    return upcount, locount



