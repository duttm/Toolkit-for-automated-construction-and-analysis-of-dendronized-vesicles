import numpy


from index import *
from index_1 import *


def rog(Mol1_array, Mol1_status, filename_mol1, group_index):


################################################################

    print("Reading Mol1......" + '\n')
    inputfilename = filename_mol1
    f = open(inputfilename, "r")
    lines = f.readlines()
    args = []
    for x in lines:
        args.append(x.split('\t')[1].strip())
    f.close()
    filename = args[0]
    fp = open(filename)
    line_count = 0
    for i, line in enumerate(fp):
        if i == 1:
            Mol1_a = int(line.strip())

        if line != "\n":
            line_count += 1

    fp.close()
    print('No. of elements in a single frame is %s' % (Mol1_a))
    Mol1_size = int(args[1])
    print('No. of elements in a single molecule is %s' % (Mol1_size))
    Mol1_NOF = int(line_count / (Mol1_a + 3))
    print('No. of frames in trajectory is %s' % (Mol1_NOF))
    Mol1_iden = args[group_index]
    print('Groups under consideration for finding effective radius %s' % (Mol1_iden))


##############################################################################

    array = Mol1_array
    s1 = int(Mol1_a / Mol1_size)
    rows, cols, s, pages = (Mol1_size, 4, s1, Mol1_NOF)
    
    ints = [int(item) for item in indices(args[3], args[group_index])]
    i1 = [x - 1 for x in ints]
    
    
    eff_rog = []

    for k in range(pages):
        d = []
        for l in range(s):
            COM1 = []
            COM2 = []
            COM3 = []
           
            if Mol1_status[k][l] == "outside":
                
                for y in range(len(i1)):
                    i = i1[y]
                    
                    COM1.append(array[i][1][l][k])
                    COM2.append(array[i][2][l][k])
                    COM3.append(array[i][3][l][k])
                    
                COM_x = (sum(COM1) /len(COM1))
                COM_y = (sum(COM2) /len(COM2))
                COM_z = (sum(COM3) /len(COM3))
                
                store = 0
                for y in range(len(i1)):
                    i = i1[y]
                    
                    a1 = numpy.array((array[i][1][l][k], array[i][2][l][k], array[i][3][l][k]))
                    a2 = numpy.array((COM_x, COM_y, COM_z))
                    r1 = numpy.linalg.norm(a1 - a2)
                    store += r1*r1
                d.append(numpy.sqrt(store/len(i1)))
                
        eff_rog.append(sum(d) /len(d))
        
        
    return eff_rog        
    
    
def rog_all(Mol1_array, Mol1_status, filename_mol1):


################################################################

    print("Reading Mol1......" + '\n')
    inputfilename = filename_mol1
    f = open(inputfilename, "r")
    lines = f.readlines()
    args = []
    for x in lines:
        args.append(x.split('\t')[1].strip())
    f.close()
    filename = args[0]
    fp = open(filename)
    line_count = 0
    for i, line in enumerate(fp):
        if i == 1:
            Mol1_a = int(line.strip())

        if line != "\n":
            line_count += 1

    fp.close()
    print('No. of elements in a single frame is %s' % (Mol1_a))
    Mol1_size = int(args[1])
    print('No. of elements in a single molecule is %s' % (Mol1_size))
    Mol1_NOF = int(line_count / (Mol1_a + 3))
    print('No. of frames in trajectory is %s' % (Mol1_NOF))
    Mol1_iden = args[8]
    print('Groups under consideration for finding effective radius %s' % (Mol1_iden))


##############################################################################

    array = Mol1_array
    s1 = int(Mol1_a / Mol1_size)
    rows, cols, s, pages = (Mol1_size, 4, s1, Mol1_NOF)
    
    ints = [int(item) for item in indices(args[7], args[8])]
    i1 = [x - 1 for x in ints]
    
    
    eff_rog = []

    for k in range(pages):
        d = []
        for l in range(s):
            COM1 = []
            COM2 = []
            COM3 = []
           
            if Mol1_status[k][l] == "outside":
                
                for y in range(len(i1)):
                    i = i1[y]
                    
                    COM1.append(array[i][1][l][k])
                    COM2.append(array[i][2][l][k])
                    COM3.append(array[i][3][l][k])
                    
                COM_x = (sum(COM1) /len(COM1))
                COM_y = (sum(COM2) /len(COM2))
                COM_z = (sum(COM3) /len(COM3))
                
                store = 0
                for y in range(len(i1)):
                    i = i1[y]
                    
                    a1 = numpy.array((array[i][1][l][k], array[i][2][l][k], array[i][3][l][k]))
                    a2 = numpy.array((COM_x, COM_y, COM_z))
                    r1 = numpy.linalg.norm(a1 - a2)
                    store += r1*r1
                d.append(numpy.sqrt(store/len(i1)))
                
        eff_rog.append(sum(d) /len(d))
        
        
    return eff_rog        
      
      

def rog_dist(Mol1_array, Mol1_status, filename_mol1, group_index):


################################################################

    print("Reading Mol1......" + '\n')
    inputfilename = filename_mol1
    f = open(inputfilename, "r")
    lines = f.readlines()
    args = []
    for x in lines:
        args.append(x.split('\t')[1].strip())
    f.close()
    filename = args[0]
    fp = open(filename)
    line_count = 0
    for i, line in enumerate(fp):
        if i == 1:
            Mol1_a = int(line.strip())

        if line != "\n":
            line_count += 1

    fp.close()
    print('No. of elements in a single frame is %s' % (Mol1_a))
    Mol1_size = int(args[1])
    print('No. of elements in a single molecule is %s' % (Mol1_size))
    Mol1_NOF = int(line_count / (Mol1_a + 3))
    print('No. of frames in trajectory is %s' % (Mol1_NOF))
    Mol1_iden = args[group_index]
    print('Groups under consideration for finding effective radius %s' % (Mol1_iden))


##############################################################################

    array = Mol1_array
    s1 = int(Mol1_a / Mol1_size)
    rows, cols, s, pages = (Mol1_size, 4, s1, Mol1_NOF)
    
    ints = [int(item) for item in indices(args[3], args[group_index])]
    i1 = [x - 1 for x in ints]
    
    
    d = []

    for k in range(pages):
 
        for l in range(s):
            COM1 = []
            COM2 = []
            COM3 = []
           
            if Mol1_status[k][l] == "outside":
                
                for y in range(len(i1)):
                    i = i1[y]
                    
                    COM1.append(array[i][1][l][k])
                    COM2.append(array[i][2][l][k])
                    COM3.append(array[i][3][l][k])
                    
                COM_x = (sum(COM1) /len(COM1))
                COM_y = (sum(COM2) /len(COM2))
                COM_z = (sum(COM3) /len(COM3))
                
                store = 0
                for y in range(len(i1)):
                    i = i1[y]
                    
                    a1 = numpy.array((array[i][1][l][k], array[i][2][l][k], array[i][3][l][k]))
                    a2 = numpy.array((COM_x, COM_y, COM_z))
                    r1 = numpy.linalg.norm(a1 - a2)
                    d.append(r1)
                
        
        
        
    return d   
  
  
def rog_dist_1(Mol1_array, Mol1_status, filename_mol1, group_index):


################################################################

    print("Reading Mol1......" + '\n')
    inputfilename = filename_mol1
    f = open(inputfilename, "r")
    lines = f.readlines()
    args = []
    for x in lines:
        args.append(x.split('\t')[1].strip())
    f.close()
    filename = args[0]
    fp = open(filename)
    line_count = 0
    for i, line in enumerate(fp):
        if i == 1:
            Mol1_a = int(line.strip())

        if line != "\n":
            line_count += 1

    fp.close()
    print('No. of elements in a single frame is %s' % (Mol1_a))
    Mol1_size = int(args[1])
    print('No. of elements in a single molecule is %s' % (Mol1_size))
    Mol1_NOF = int(line_count / (Mol1_a + 3))
    print('No. of frames in trajectory is %s' % (Mol1_NOF))
    Mol1_iden = args[group_index]
    print('Groups under consideration for finding effective radius %s' % (Mol1_iden))


##############################################################################

    array = Mol1_array
    s1 = int(Mol1_a / Mol1_size)
    rows, cols, s, pages = (Mol1_size, 4, s1, Mol1_NOF)
    
    ints = [int(item) for item in indices(args[3], args[group_index])]
    i1 = [x - 1 for x in ints]
    
    
    d = []
    
    j = int(index(args[3], args[4])) - 1

    for k in range(pages):
 
        for l in range(s):
       
           
            if Mol1_status[k][l] == "outside":
                
                for y in range(len(i1)):
                    i = i1[y]
                    
                    a1 = numpy.array((array[i][1][l][k], array[i][2][l][k], array[i][3][l][k]))
                    a2 = numpy.array((array[j][1][l][k], array[j][2][l][k], array[j][3][l][k]))
                    r1 = numpy.linalg.norm(a1 - a2)
                    d.append(r1)
                
        
        
        
    return d   
