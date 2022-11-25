from index import *


def FindCOM(array_4D, filename, NOF, a, size, newfile, moleculefile, indexing):


    array = array_4D
    s1 = int(a / size)
    rows, cols, s, pages = (size, 4, s1, NOF)

    m, n = (NOF, 3)
    Com_matrix = [[0 for i in range(n)] for j in range(m)]



    for k in range(NOF):
        for l in range(s):

            i = int(index(moleculefile, indexing)) - 1
            Com_matrix[k][0] += array[i][1][l][k]
            Com_matrix[k][1] += array[i][2][l][k]
            Com_matrix[k][2] += array[i][3][l][k]

        Com_matrix[k][0] /= s
        Com_matrix[k][1] /= s
        Com_matrix[k][2] /= s



    return Com_matrix