def vesicle_status(rad, uprad, upcount, lorad, locount, expelled, NOF):

    output_textfile = "vesicle_status.txt"
    file_out4d = open(output_textfile, "w")

    file_out4d.writelines("Mean Radius" + '\t' + "Outer_Ro" + '\t' + "Outer_No" + '\t' + "Inside_Ro" + '\t' + "Inside_No" + '\t' + "Expelled" +'\n' )

    for k in range(NOF):
        file_out4d.writelines('{:8.3f}'.format(rad[k]) + '\t ' + '{:8.3f}'.format(uprad[k]) + '\t ' + '{:8.0f}'.format(upcount[k]) + '\t' + '{:8.3f}'.format(lorad[k]) + '\t' + '{:8.0f}'.format(locount[k]) + '\t' + '{:8.0f}'.format(expelled[k]) + '\n')
    file_out4d.close()