# Importing Pandas to create DataFrame
import pandas as pd
import sys



###############################################################
arguments = len(sys.argv) - 1
Base_directory=sys.argv[1] + "/Collection"
PH= ["ACIDIC", "BASIC"]
##PH= ["ACIDIC"]

FEATURE= ["ROG_DENS_TA", "TA-TA", "TA-PO4", "Den_layer_thickness", "DHS_TAbeads", "AND_results", "hydrophobic_vol", "packing_factor", "Thickness_Bilayer"]
##GEN= ["G1"]
GEN= ["G1", "G2", "G3", "G4", "G5", "G6"]





###################################


##############################################################

# Creating Empty DataFrame and Storing it in variable df

col_list=['Generation', 'pH', 'Concentration', "ROG_DENS_TA", "TA-TA", "TA-PO4", "Den_layer_thickness", "DHS_TAbeads", "AND_results", "hydrophobic_vol", "packing_factor", "Thickness_Bilayer"]
df = pd.DataFrame(columns=col_list)

# Printing Empty DataFrame
##print(df)

##############################################################

## Count number of rows 

row_count = 0
conc_array = []


for i in range(len(GEN)):
    for j in range(len(PH)):
        
        for k in range(1):
            name_file = GEN[i] + '_' + PH[j] + '_' + FEATURE[k] + '.txt'     
            location =  Base_directory + '/' + name_file
            
            f2=open(location,"r")
            lines = f2.readlines()
            
            conc_counter = 0
            for x in lines:
            
                row_count += 1
                conc_counter += 1
                
            conc_array.append(conc_counter)
            
            
print(conc_array)
print(row_count)              
#################################################################

rows, cols = (row_count, len(col_list))
array = [[0 for i in range(cols)] for j in range(rows)]
    
    
i=0

for j in range(len(GEN)):
    for k in range(len(PH)):
        for l in range(1):
            
            
            
            name_file = GEN[j] + '_' + PH[k] + '_' + FEATURE[l] + '.txt'     
            location =  Base_directory + '/' + name_file
            
            f2=open(location,"r")
            lines = f2.readlines()
            
            
            for x in lines:
            
                array[i][0] = x.split()[0].strip()
                array[i][1] = x.split()[1].strip()
                array[i][2] = x.split()[2].strip()
                
                for m in range(len(FEATURE)):
                    feature_file = GEN[j] + '_' + PH[k] + '_' + FEATURE[m] + '.txt'     
                    location =  Base_directory + '/' + feature_file
            
                    f3=open(location,"r")
                    lines = f3.readlines()
            
                    for x1 in lines:
                        if (array[i][0] == x1.split()[0].strip() and array[i][1] == x1.split()[1].strip() and array[i][2] == x1.split()[2].strip()):
                            array[i][m+3] = x1.split()[3].strip()
                    
                        
                    f3.close()
                    
                i += 1        
                
            f2.close()
                
                                 
           
#############################

file_out=open("array.txt","w")

for i in range(len(col_list)):
    file_out.write(col_list[i]+ ',')
    
file_out.write('\n')
    
for i in range(rows):
    for j in range(cols):
        file_out.write(str(array[i][j]) + ',')
    file_out.write('\n')    
file_out.close()


###############################################################

