import numpy
from index import *


def radiusfinder(COM, array_4D, filename, NOF, a, size, outfile, moleculefile, indexing):
    array = array_4D
    s1 = int(a / size)
    rows, cols, s, pages = (size, 4, s1, NOF)

    m, n = (NOF, s)
    radius_is = [0 for i in range(m)]
    raw_radius = [[0 for i in range(n)] for j in range(m)]

    expelled = [0 for i in range(m)]
    status = [[0 for i in range(n)] for j in range(m)]

    upcount = [0 for i in range(m)]
    locount = [0 for i in range(m)]

    upradius = [0 for i in range(m)]
    loradius = [0 for i in range(m)]


    for k in range(NOF):
        mean = 0
        for l in range(s):
            i = int(index(moleculefile, indexing)) - 1
            a = numpy.array((COM[k][0], COM[k][1], COM[k][2]))
            b = numpy.array((array[i][1][l][k], array[i][2][l][k], array[i][3][l][k]))

            raw_radius[k][l] = numpy.linalg.norm(a - b)
            mean += numpy.linalg.norm(a - b)

        mean = mean / s

        observations = 0

        for l in range(s):
            if raw_radius[k][l] < 2 * mean:
                radius_is[k] += raw_radius[k][l]
                observations = observations + 1

        radius_is[k] = radius_is[k] / observations


        for l in range(s):
            if raw_radius[k][l] < radius_is[k]:
                status[k][l] = "inside"
                locount[k] += 1
                loradius[k] += raw_radius[k][l]
            elif raw_radius[k][l] > radius_is[k] and raw_radius[k][l] < 2 * mean:
                status[k][l] = "outside"
                upcount[k] += 1
                upradius[k] += raw_radius[k][l]
            elif raw_radius[k][l] >= 2 * mean:
                status[k][l] = "expelled"
                expelled[k] += 1
        loradius[k] /= locount[k]
        upradius[k] /= upcount[k]
    return radius_is, upradius, upcount, loradius, locount, expelled, status



