import numpy
from index import *

def onedresult(array, measureable, NOF, output_textfile):


    file_out = open(output_textfile, "w")

    file_out.writelines("Frame" + '\t' + measureable + '\n')
    for k in range(NOF):
        file_out.writelines(str(k + 1) + '\t' + str(array[k]) + '\n')
    file_out.close()

def onedresult_1(array, array1, measureable, NOF, output_textfile):


    file_out = open(output_textfile, "w")

    file_out.writelines("Frame" + '\t' + measureable + '\n')
    for k in range(NOF):
        file_out.writelines(str(k + 1) + '\t' + str(array[k]-array1[k]) + '\n')
    file_out.close()

def onedresult_2(array, measureable, NOF, output_textfile):


    file_out = open(output_textfile, "w")

    file_out.writelines("Frame" + '\t' + measureable + '\n')
    for k in range(len(array)):
        file_out.writelines(str(k + 1) + '\t' + str(array[k]) + '\n')
    file_out.close()
