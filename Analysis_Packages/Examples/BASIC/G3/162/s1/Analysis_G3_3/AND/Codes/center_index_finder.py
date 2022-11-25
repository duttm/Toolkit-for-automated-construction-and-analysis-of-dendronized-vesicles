from index import *

def center_index_finder(array_4D, status, NOF,a, size, moleculefile, indexing):

    s1 = int(a / size)
    rows, cols, s, pages = (size, 4, s1, NOF)

    m, n = (NOF, s)

    for k in range(NOF):
        for l in range(s):
            if status[k][l] == "inside":
                Record_frame = k
                Record_molecule = l

    i = int(index(moleculefile, indexing)) - 1
    spotted = array_4D[i][0][Record_molecule][Record_frame]

    output_textfile = "center_index_number.txt"
    file_out = open(output_textfile, "w")
    file_out.writelines("Center is at serial number:" + '\t' + str(int(spotted)))
    
    file_out.close()
