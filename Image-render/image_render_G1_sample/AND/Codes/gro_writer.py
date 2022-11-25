from array import array


def gro_writer(array_4D, rem_4D, status, a, size, Mol2_4d_array, Mol2_4d_array_rem, Mol2_status, mol2_a, mol2_size, NOF, boxx, boxy, boxz):
  
  
    s1 = int(mol2_a / mol2_size)

    rows, cols, s, pages = (mol2_size, 4, s1, NOF) 
  


    D1 = []
    D2 = []
    D3 = []
    D4 = array('i')
    D5 = []
    D6 = []
    D7 = []
    
    m=1

    for k in range(NOF):
        for l in range(s):
            for i in range(rows): 
                if (Mol2_status[k][l] != "expelled"):
                    D1.append(int(Mol2_4d_array_rem[i][1][l][k]))
                    D2.append(Mol2_4d_array_rem[i][2][l][k])
                    D3.append(Mol2_4d_array_rem[i][3][l][k])
                    D4.append(m)
                    D5.append(float(Mol2_4d_array[i][1][l][k]))
                    D6.append(float(Mol2_4d_array[i][2][l][k]))
                    D7.append(float(Mol2_4d_array[i][3][l][k]))
                    m = m + 1
                    
                
    s1 = int(a / size)

    rows, cols, s, pages = (size, 4, s1, NOF)   

    for k in range(NOF):
        for l in range(s):
            for i in range(rows): 
                if (status[k][l] != "expelled"):
                    D1.append(int(rem_4D[i][1][l][k]))
                    D2.append(rem_4D[i][2][l][k])
                    D3.append(rem_4D[i][3][l][k])
                    D4.append(m)
                    D5.append(float(array_4D[i][1][l][k]))
                    D6.append(float(array_4D[i][2][l][k]))
                    D7.append(float(array_4D[i][3][l][k]))
                    m = m + 1
            

    file_write_gro = open("write.gro", "w")

  

    file_write_gro.writelines('we are making a grid' + '\n')
    file_write_gro.write(str(m - 2) + '\n')
    for k in range(m - 2):
        file_write_gro.writelines(
            '{:>5}'.format(str(D1[k])) + '{:>5}'.format(str(D2[k])) + '{:>5}'.format(str(D3[k])) + '{:>5}'.format(
                str(D4[k])) + '{:8.3f}'.format(D5[k]) + '{:8.3f}'.format(D6[k]) + '{:8.3f}'.format(D7[k]) + '\n')

    file_write_gro.writelines('{:8.3f}'.format(boxx) + '{:8.3f}'.format(boxy) + '{:8.3f}'.format(boxz))
    file_write_gro.close()
