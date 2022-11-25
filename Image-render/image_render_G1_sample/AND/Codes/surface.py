import numpy
from index import *


def surfacecalc(Mol2_Mol1_interaction, uprad, NOF, output_textfile):
    file_out = open(output_textfile, "w")
    file_out.writelines(
        "{:<40} {:<40} {:<40}".format("Fraction of interaction surface(A)", "Tot surface area(B)", "A*B")+'\n')
    for k in range(NOF):

        file_out.writelines(
            "{:<40} {:<40} {:<40}".format('{:8.3f}'.format(Mol2_Mol1_interaction[k]), '{:8.3f}'.format(4 * 3.14 * (uprad[k] ** 2)),
                                          '{:8.3f}'.format(Mol2_Mol1_interaction[k] * 4 * 3.14 * (uprad[k] ** 2))) + '\n')


    file_out.close()
