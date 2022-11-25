def status_writer(status, NOF,a, size, output_textfile):

    array = status
    s1 = int(a / size)
    rows, cols, s, pages = (size, 4, s1, NOF)

    m, n = (NOF, s)

    status = [[0 for i in range(n)] for j in range(m)]

    file_out = open(output_textfile, "w")
    file_out.writelines("Frame" + '\t' + "Status"  + '\n')
    for k in range(NOF):
        for l in range(s):
            file_out.writelines(str(k+1) + '\t' + str(array[k][l]) + '\n')

        file_out.writelines('\n')    # view array.txt to check
    file_out.close()

