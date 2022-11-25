import os
import sys

import shutil

import subprocess

from pathlib import Path

import statistics

import math           

arguments = len(sys.argv) - 1
nameofstudy="DEN_vesicle_status"
Analysis=nameofstudy+ ".out"
analysis_dir= "Comb_Outs"

inputfilename = sys.argv[1]

f=open(inputfilename,"r")
lines=f.readlines()

generation=[]

for x in lines:
    generation.append(x.strip())
f.close()



print(generation)


print("Current directory :", os.getcwd())

    
basedirectory=os.getcwd()

path_to_records=basedirectory + '/' + nameofstudy
isExist = os.path.exists(path_to_records)
if not isExist:
    subprocess.check_call(['mkdir', nameofstudy])
            
for i in range(len(generation)):  
    
   

    
    destination= basedirectory +'/'+ generation[i]
    os.chdir(destination)
    
    fileobject='G' + str(i+1)
    nameofsummary='Summary' + fileobject + '.txt'
    
    fileobject=open(nameofsummary,"w")
    
    f=open('G' + str(i+1) + '.txt',"r")
    lines=f.readlines()

    concentration=[]
    seeds=[]

    for x in lines:
        print(x)
        concentration.append(x.split(' ')[0])
        seeds.append(int(x.split(' ')[1].strip()))
    f.close()
    
    noc = len(concentration)

    for j in range(noc):
    
        outputstorage=[]
        concdir= concentration[j]
        concdestination= destination +'/'+ concdir
        os.chdir(concdestination)
    
        print("Current directory :", os.getcwd())
        
        
        nos = seeds[j]
        
        
        
        for k in range(nos):
    
            seeddir= "c" + str(k)
            seeddestination= concdestination + '/' + seeddir
            os.chdir(seeddestination)
            
         
            print("Current directory :", os.getcwd())
            
            Fin1 =  seeddestination + '/' + analysis_dir
            
            Fin2 =  seeddestination + '/' + analysis_dir + '/' + Analysis
            ##############################################
            
            
            isExist = os.path.exists(Fin2)
            
            if isExist:
                os.chdir(Fin1)
                     
                f2=open(Analysis,"r")
            
                AND=[]
                lines = f2.readlines()[1:]
                for x in lines:
                    AND.append(float(x.split()[5].strip()) / ( (float(x.split()[4].strip())) + (float(x.split()[5].strip())) + (float(x.split()[2].strip())) ) )
                f2.close()    
            
                nameofoutput=generation[i] + '_' + concentration[j] + '_' + 's' + str(k) + '.txt'
  
                with open(nameofoutput, 'w') as f:
                    for item in AND:
                        f.write("%s\n" % item)
                f.close()        
            
         

                src = os.getcwd()
                trg = concdestination
 
                fname = nameofoutput
                outputstorage.append(fname)
            
                shutil.copy2(os.path.join(src,fname), trg)
            
        os.chdir(concdestination)
        print("Current directory :", os.getcwd())
        # Open file3 in write mode
        with open('concatenated.txt', 'w') as outfile:
            for names in outputstorage:
                with open(names) as infile:
                    outfile.write(infile.read())
                    
        f=open('concatenated.txt',"r")
        lines=f.readlines()

        concat=[]

        for x in lines:
            concat.append(float(x.strip()))
        f.close()
        
        mean=statistics.mean(concat)
        ##ste=statistics.stdev(concat)/math.sqrt(len(concat))
        ste=statistics.stdev(concat)
        
        print(mean,ste)
        
        fileobject.write('G' + str(i+1) + ' ' + concentration[j] + ' '+ str(mean) + ' '+ str(ste) + '\n' )
        
    fileobject.close()      
    
    shutil.copy(destination + '/' + nameofsummary, path_to_records)
    

          
    
    

              
            
         
        
